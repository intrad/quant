Authors:-      FRM, Pranav Gandhi               
Date:-         05 May 2017

Intro
--------------------
This is simple impractical but realistic implementation of simple moving average crossover strategy. This documents provides some basic documentation on code, input, output and assumptions.
Quant package defines 3 python files.

1) portfolio.py:
	Defines hypthetical portfolio class with ability to set initial cash amout to start with and dictionary of stocks.
	
2) strategy.py:
	Defines SMACrossoverStrategy class that accepts short and long lookback windos and generates signals( 1(buy), 0(hold),-1(sell) ) in pandas dataframe which is used by backtest to calculate returns and running positions.
	Defines MarketData class with methods to fetch timeseries data for any given stock from file or from quandl.
	
3) backtest.py:
	Defines BackTest class that accepts given portfolio and signals and defines method to backtest and generates backtesting report.

Assumptions
--------------------
	- Initial Cash Balance of Portfolio = 1000
	- Supports multistocks
	- Negative cash implies you are allowed to borrow cash interest free.
	- Negative stock quantity implies short selling is allowed
	- Portfolio compises of cash and stocks trading in any exchange but can be valued in single currency in single currency eg. Rs.
	- No transaction costs
	- No brokerages
	
	
Required Package Files
--------------------
quandl: fetching timeseries data for backtesting
matplotlib: Ploting charts
pandas: Computations
numpy: Computations
tempfile: IO operations
os: IO Operations