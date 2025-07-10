# Cross-Sectional Mean Reversion Strategy using Backtrader

This project implements a **cross-sectional mean reversion strategy** using the Backtrader backtesting framework. The strategy dynamically adjusts portfolio weights based on the relative daily returns of a basket of stocks.

## 📈 Overview

**Cross-sectional mean reversion** involves comparing asset returns within a group to the average market return. Assets that outperform the group are sold short, and underperformers are bought long — assuming they will revert to the mean.

## 🧠 Strategy Logic

At each timestep:
1. Calculate daily returns for each stock.
2. Compute the average return across all stocks.
3. Assign portfolio weights as the negative deviation from the average.
4. Normalize weights to sum to 1 and update positions accordingly.


## 📌 Requirements

```bash
pip install backtrader pandas numpy
```

## Sample:

Initial capital: $10000.00
Sharpe ratio: 0.88
Return: 32.50%
Max Drawdown: 12.40%
Capital: $13250.00

## ⚠️ Notes

  The strategy requires at least 100 data points per stock.

  CSV files must be correctly formatted with Date as the index.
  
  It does not include transaction cost, slippage, or market impact modeling.
