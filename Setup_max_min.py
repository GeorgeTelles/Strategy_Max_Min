"""
Esse codigo faz um backteste usando as estrategias de maximas e minimas
ele puxa os dados do Yahoo finance e faz as simulações.

By: George Telles
+55 11 93290-7425
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

ticker = 'ITUB4.SA'
start = '2015-01-01'
end = '2023-08-30'
df = yf.download(ticker, start, end)[["Open", "High", "Low", "Close"]]
df

df["Target1"] = df["High"].shift(1)
df["Target2"] = df["High"].shift(2)
df["Target"] = df[["Target1", "Target2"]].max(axis=1)

# We don't need them anymore
df.drop(columns=["Target1", "Target2"], inplace=True)


df["Entry1"] = df["Low"].shift(1)
df["Entry2"] = df["Low"].shift(2)
df["Entry"] = df[["Entry1", "Entry2"]].min(axis=1)

# We don't need them anymore
df.drop(columns=["Entry1", "Entry2"], inplace=True)

df.head()

# Define exact buy price
df['Buy Price'] = np.where(
    df["Low"] < df['Entry'],
    np.where((df['Open'] < df['Entry']), df['Open'], df['Entry']),
    np.nan)

# Define exact sell price
df['Sell Price'] = np.where(
    df["High"] > df['Target'], 
    np.where(df['Open'] > df['Target'], df['Open'], df['Target']),
    np.nan)

df.head(10)

# Define control variable for ongoing operations
ongoing = False

for i in range(0,len(df)):

    # If there is an ongoing operation, check if we reached the target price
    if ongoing == True:
        if ~(np.isnan(df['Sell Price'][i])):
            exit = df['Sell Price'][i]
            ongoing = False

    # If there is no ongoing operation, check if the entry price was achieved
    else:
        if ~(np.isnan(df['Buy Price'][i])):
            entry = df['Buy Price'][i]
            ongoing = True

import math

# Create a function to round any number to the smalles multiple of 100
def round_down(x):
  return int(math.floor(x / 100.0)) * 100

# Define backtest parameters
initial_capital = 10000
max_days = 3 # add stop in time

# Control variables
total_capital = [initial_capital] # list with the total capital after every operation
all_profits = [] # list with profits for every operation
days_in_operation = 0
gains_total_days = 0
gains_total_operations = 0
losses_total_days = 0
losses_total_operations = 0
ongoing = False  

for i in range(0,len(df)):
    if ongoing == True:
        days_in_operation += 1

        # If any of the following conditions are met, the operation will end
        if days_in_operation == max_days or ~(np.isnan(df['Sell Price'][i])):

            # Define exit point and total profit
            exit = np.where(
                ~(np.isnan(df['Sell Price'][i])), 
                df['Sell Price'][i], 
                df['Close'][i])
            profit = shares * (exit - entry)

            # Append profit to list and create a new entry with the capital
            # after the operation is complete
            all_profits += [profit]
            current_capital = total_capital[-1]
            total_capital += [current_capital + profit]

            # If profit is positive we increment the gains' variables
            # Else, we increment the losses' variables
            if profit > 0:
                gains_total_days += days_in_operation
                gains_total_operations += 1
            else: 
                losses_total_days += days_in_operation
                losses_total_operations += 1
            
            ongoing = False
    else:
        if ~(np.isnan(df['Buy Price'][i])):
            entry = df['Buy Price'][i]
            shares = round_down(initial_capital / entry)
            days_in_operation = 0
            ongoing = True

def strategy_test(all_profits): 
  num_operations = len(all_profits)
  gains = sum(x >= 0 for x in all_profits)
  pct_gains = 100 * (gains / num_operations)
  losses = num_operations - gains
  pct_losses = 100 - pct_gains

  print("Number of operations =", num_operations)
  print("Number of gains =", gains, "or", pct_gains.round(), "%")
  print("Number of loss =", losses, "or", pct_losses.round(), "%")
  print("The total profit was = R$", sum(all_profits))

strategy_test(all_profits)

total_days = gains_total_days + losses_total_days
total_operations = gains_total_operations + losses_total_operations

print("Average length of operations (in days)", total_days / total_operations)
print("Average length of gains (in days)", gains_total_days / gains_total_operations)
print("Average length of losses (in days)", losses_total_days / losses_total_operations)



def capital_plot(total_capital, all_profits):
  all_profits = [0] + all_profits # make sure both lists are the same size
  cap_evolution = pd.DataFrame({'Capital': total_capital, 'Profit': all_profits})
  plt.title("Curva de Capital")
  plt.xlabel("Total Operações")
  cap_evolution['Capital'].plot()
  plt.show()

capital_plot(total_capital, all_profits)
