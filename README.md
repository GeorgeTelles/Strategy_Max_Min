<div>
  <img src="https://raw.githubusercontent.com/GeorgeTelles/georgetelles/f69531ec6b293b5148563588a764c010015d315e/logo_clara.png" alt="logo clara" width="300" style="display: inline-block; vertical-align: top; margin-right: 10px;">
  <img src="https://raw.githubusercontent.com/GeorgeTelles/georgetelles/f69531ec6b293b5148563588a764c010015d315e/logo_dark.png" alt="logo dark" width="300" style="display: inline-block; vertical-align: top;">
</div>

# Strategy Backtesting: Max and Min

## Description

In financial markets, various strategies are employed to determine buy and sell points through technical analysis of an asset's price chart. One such strategy is the Maxima and Minima strategy, which is the focus of this project.

The Maxima and Minima strategy is based on setting the buy price at the lowest low of the previous two days and the sell price at the highest high of the previous two days. This approach aims to identify potential entry and exit points for trading based on historical price data.

## Project Features

- **Data Collection**: Retrieve historical price data for financial assets (stocks, currencies, etc.).
  
- **Data Modeling and Column Creation**: Create columns representing the two most recent highs and lows for each candle, then determine entry and exit points based on these values. The buy price (entry point) is set at the lowest low of the previous two days, while the sell price (exit point) is set at the highest high of the previous two days.

- **Buy and Sell Price Definition**: Calculate exact buy and sell prices based on the conditions established by the strategy.

- **Backtesting**: Simulate the strategy on historical data to evaluate its performance. This includes tracking ongoing operations, calculating profits and losses, and determining key performance metrics.

- **Profit Calculation and Analysis**: Assess the total profit, percentage gains and losses, and the performance of the holding strategy compared to the strategy. 

- **Visualization**: Generate a capital curve plot to visualize the evolution of capital over time and assess the effectiveness of the strategy.

## Technologies Used

- **Language**: Python

- **Libraries**:
  - `pandas` for data manipulation
  - `numpy` for numerical calculations
  - `matplotlib` for visualization
  - `yfinance` for financial data retrieval

- **Development Environment**: Jupyter Notebook or your preferred IDE

## Project Structure

1. **Importing Libraries**: Import necessary libraries for data manipulation, calculations, and visualization.
   
2. **Obtaining Data**: Download historical price data for the chosen asset.

3. **Data Modeling**: Create columns for the two most recent highs and lows, calculate entry and exit points, and define exact buy and sell prices.

4. **Backtesting**: Simulate the strategy, track ongoing operations, and evaluate performance metrics such as total profit, average length of operations, and percentage of gains versus losses.

5. **Results Analysis**: Analyze the performance of the strategy, including total and percentage profits, average operation durations, and comparison with a holding strategy.

6. **Visualization**: Plot the capital evolution over time to visualize the results of the backtesting.

## Results

The results include detailed metrics on the number of operations, percentage of gains and losses, total profit, and a comparison with a holding strategy. The capital evolution plot provides a visual representation of the strategy’s performance over time.

-------------------------------------------------------------------------------------------------------------------------------------

# Backtesting da Estratégia: Máximas e Mínimas

## Descrição

No mercado financeiro, diversas estratégias são empregadas para determinar pontos de compra e venda por meio da análise técnica do gráfico de preços de um ativo. Uma dessas estratégias é a estratégia de Máximas e Mínimas, que é o foco deste projeto.

A estratégia de Máximas e Mínimas baseia-se em definir o preço de compra na mínima dos dois dias anteriores e o preço de venda na máxima dos dois dias anteriores. Esta abordagem visa identificar possíveis pontos de entrada e saída para negociações com base em dados históricos de preços.

## Funcionalidades do Projeto

- **Coleta de Dados**: Obter dados históricos de preços de ativos financeiros (ações, moedas, etc.).

- **Modelagem dos Dados e Criação de Colunas**: Criar colunas que representam as duas últimas máximas e mínimas de cada candle, e então definir os pontos de entrada e saída com base nesses valores. O preço de compra (ponto de entrada) é definido pela mínima dos dois dias anteriores, enquanto o preço de venda (ponto de saída) é definido pela máxima dos dois dias anteriores.

- **Definição dos Preços de Compra e Venda**: Calcular preços exatos de compra e venda com base nas condições estabelecidas pela estratégia.

- **Backtesting**: Simular a estratégia com dados históricos para avaliar seu desempenho. Isso inclui o acompanhamento das operações em andamento, cálculo de lucros e perdas, e determinação de métricas de desempenho chave.

- **Cálculo e Análise dos Lucros**: Avaliar o lucro total, ganhos e perdas percentuais, e comparar o desempenho da estratégia com o de uma estratégia de holding (manutenção).

- **Visualização**: Gerar um gráfico da curva de capital para visualizar a evolução do capital ao longo do tempo e avaliar a eficácia da estratégia.

## Tecnologias Utilizadas

- **Linguagem**: Python

- **Bibliotecas**:
  - `pandas` para manipulação de dados
  - `numpy` para cálculos numéricos
  - `matplotlib` para visualização
  - `yfinance` para coleta de dados financeiros

- **Ambiente de Desenvolvimento**: Jupyter Notebook ou IDE de sua escolha

## Estrutura do Projeto

1. **Importação de Bibliotecas**: Importar as bibliotecas necessárias para manipulação de dados, cálculos e visualização.
   
2. **Obtenção de Dados**: Baixar dados históricos de preços para o ativo selecionado.

3. **Modelagem dos Dados**: Criar colunas para as duas últimas máximas e mínimas, calcular pontos de entrada e saída, e definir os preços exatos de compra e venda.

4. **Backtesting**: Simular a estratégia, acompanhar operações em andamento e avaliar métricas de desempenho como lucro total, duração média das operações e porcentagem de ganhos versus perdas.

5. **Análise dos Resultados**: Analisar o desempenho da estratégia, incluindo lucro total e percentual, duração média das operações e comparação com a estratégia de holding.

6. **Visualização**: Plotar a evolução do capital ao longo do tempo para visualizar os resultados do backtesting.

## Resultados

Os resultados incluem métricas detalhadas sobre o número de operações, porcentagem de ganhos e perdas, lucro total e uma comparação com a estratégia de holding. O gráfico da evolução do capital fornece uma representação visual do desempenho da estratégia ao longo do tempo.


