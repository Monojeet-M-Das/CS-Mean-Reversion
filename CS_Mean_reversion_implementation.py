import backtrader as bt
import numpy as np
import pandas as pd
import os

class CrossSectionalMeanReversion(bt.Strategy):
    def __init__(self):
        self.stock_data = self.datas

    def prenext(self):
        self.next()
    
    def next(self):
        stock_returns = np.zeros(len(self.stock_data))

        # calculate the last daily returns
        for index, stock in enumerate(self.stock_data):
            stock_returns[index] = (stock.close[0] -stock.close[-1]) / stock.close[-1]

        # average return of the market (SP500)
        market_return = np.mean(stock_returns)
        # weights
        weights = -(stock_returns - market_return)
        weights = weights / np.sum(np.abs(weights))

        # we can update our postitions based on w weights
        for index, stock in enumerate(self.stock_data):
            self.order_target_percent(stock, target=weights[index])

if __name__ == '__main__':

    cerebro = bt.Cerebro()

    # Read ticker symbols from file
    with open("companies_cross_sectional") as file_in:
        for line in file_in:
            try:
                ticker = line.strip('\n')
                df = pd.read_csv(ticker, parse_dates=True, index_col=0)

                if len(df) > 100:
                    cerebro.adddata(bt.feeds.PandasData(dataname=df, plot=False))
            except FileNotFoundError:
                pass


    cerebro.addobserver(bt.observers.Value)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, riskfreerate= 0)
    cerebro.addanalyzer(bt.analyzers.Returns)
    cerebro.addanalyzer(bt.analyzers.DrawDown)

    cerebro.addstrategy(CrossSectionalMeanReversion)
    cerebro.broker.set_cash(10000)
    print('initial capital: $%.2f' % cerebro.broker.getvalue())

    results = cerebro.run()
    
    print('Sharpe ratio: %.2f' % results[0].analyzers.sharperatio.get_analysis()['sharperatio'])
    print('Return: %.2f%%' % results[0].analyzers.returns.get_analysis()['rnorm100'])
    print('Max Drawdown: %.2f%%' % results[0].analyzers.drawdown.get_analysis()['max']['drawdown'])
    print('Capital: $%.2f' % cerebro.broker.getvalue())



