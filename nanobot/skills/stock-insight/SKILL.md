---
name: stock-insight
description: "Research and analyze stocks, ETFs, and market trends. Get financial data, company information, price history, and market news. Use for investment research only - always include disclaimers about not being financial advice."
metadata: {"nanobot":{"emoji":"📈","requires":{"bins":["python3"]},"always":false,"install":[{"id":"pip","kind":"pip","package":"yfinance","bins":["python3"],"label":"Install yfinance (pip)"},{"id":"pip2","kind":"pip","package":"pandas","bins":["python3"],"label":"Install pandas (pip)"}]}}
---

# Stock Insight Skill

Research and analyze stocks, ETFs, and market trends. Use this skill for investment research and educational purposes.

**IMPORTANT DISCLAIMER**: This skill provides information for research purposes only. It is NOT financial advice. Always include a disclaimer when sharing stock insights: "This is not financial advice. Do your own research before making investment decisions."

## Installation

```bash
pip install yfinance pandas
```

## Getting Stock Data

### Get current price and basic info:

```python
import yfinance as yf

ticker = yf.Ticker("AAPL")
info = ticker.info

print(f"Current Price: {info.get('currentPrice')}")
print(f"Market Cap: {info.get('marketCap')}")
print(f"P/E Ratio: {info.get('trailingPE')}")
print(f"Dividend Yield: {info.get('dividendYield')}")
print(f"52-Week High: {info.get('fiftyTwoWeekHigh')}")
print(f"52-Week Low: {info.get('fiftyTwoWeekLow')}")
print(f"Volume: {info.get('volume')}")
print(f"Avg Volume: {info.get('averageVolume')}")
```

### Get historical price data:

```python
import yfinance as yf

# Get 1 year of daily data
stock = yf.download("AAPL", period="1y")

print(stock.tail(30))  # Last 30 days
print(f"Current: {stock['Close'].iloc[-1]}")
print(f"30 days ago: {stock['Close'].iloc[-30]}")
print(f"Change: {((stock['Close'].iloc[-1] / stock['Close'].iloc[-30]) - 1) * 100:.2f}%")
```

### Get company information:

```python
import yfinance as yf

ticker = yf.Ticker("AAPL")
info = ticker.info

print(f"Company: {info.get('longName')}")
print(f"Sector: {info.get('sector')}")
print(f"Industry: {info.get('industry')}")
print(f"Description: {info.get('longBusinessSummary', '')[:500]}")
print(f"CEO: {info.get('ceo')}")
print(f"Employees: {info.get('fullTimeEmployees')}")
```

### Get financial statements:

```python
import yfinance as yf

ticker = yf.Ticker("AAPL")

# Income statement
income = ticker.income_stmt
print(income)

# Balance sheet
balance = ticker.balance_sheet
print(balance)

# Cash flow
cashflow = ticker.cashflow
print(cashflow)
```

### Get quarterly earnings:

```python
import yfinance as yf

ticker = yf.Ticker("AAPL")

# Quarterly earnings
earnings = ticker.quarterly_earnings
print(earnings)

# Earnings dates
calendar = ticker.earnings_dates
print(calendar)
```

### Get recommendations:

```python
import yfinance as yf

ticker = yf.Ticker("AAPL")

# Analyst recommendations
recs = ticker.recommendations
print(recs)

# Major holders
holders = ticker.major_holders
print(holders)
```

### Get options data:

```python
import yfinance as yf

ticker = yf.Ticker("AAPL")

# Options expiration dates
dates = ticker.options
print(dates)

# Options for specific date
if dates:
    opt = ticker.option_chain(dates[0])
    print("Calls:", opt.calls.head())
    print("Puts:", opt.puts.head())
```

## Analyzing Multiple Stocks

### Compare multiple stocks:

```python
import yfinance as yf
import pandas as pd

tickers = ["AAPL", "GOOGL", "MSFT", "AMZN"]
data = yf.download(tickers, period="1y")['Close']

# Calculate returns
returns = (data / data.iloc[0] - 1) * 100
print(returns.tail())

# Summary stats
print("\nSummary:")
for ticker in tickers:
    ret = returns[ticker].iloc[-1]
    print(f"{ticker}: {ret:.2f}%")
```

### Get sector performance:

```python
import yfinance as yf

# Popular ETFs by sector
sectors = {
    "Tech": "XLK",
    "Healthcare": "XLV", 
    "Financials": "XLF",
    "Energy": "XLE",
    "Consumer": "XLY"
}

for name, ticker in sectors.items():
    stock = yf.Ticker(ticker)
    info = stock.info
    print(f"{name}: ${info.get('currentPrice')} ({info.get('regularMarketChangePercent')}%)")
```

## Market Overview

### Get market indices:

```python
import yfinance as yf

indices = {
    "S&P 500": "^GSPC",
    "Dow Jones": "^DJI",
    "NASDAQ": "^IXIC",
    "Russell 2000": "^RUT"
}

for name, ticker in indices.items():
    idx = yf.Ticker(ticker)
    info = idx.info
    print(f"{name}: {info.get('currentPrice'):.2f} ({info.get('regularMarketChangePercent'):+.2f}%)")
```

### Get market movers:

```python
import yfinance as yf

# Top gainers (use popular stocks as example)
gainers = ["NVDA", "AMD", "TSLA", "META"]
for ticker in gainers:
    stock = yf.Ticker(ticker)
    info = stock.info
    change = info.get('regularMarketChangePercent', 0)
    print(f"{ticker}: {info.get('currentPrice')} ({change:+.2f}%)")
```

## News and Events

### Get recent news:

```python
import yfinance as yf

ticker = yf.Ticker("AAPL")
news = ticker.news

for item in news[:5]:
    print(f"Title: {item.get('title')}")
    print(f"Publisher: {item.get('publisher')}")
    print(f"Link: {item.get('link')}")
    print()
```

## Key Metrics Explained

When analyzing stocks, consider these metrics:

- **P/E Ratio**: Price-to-earnings ratio. Higher may mean overvalued or expected growth.
- **Market Cap**: Total market value. Large cap > $10B, mid cap $2-10B, small cap < $2B.
- **Dividend Yield**: Annual dividend / stock price. Higher = more income.
- **52-Week Range**: Shows volatility and current position in range.
- **Volume**: Number of shares traded. Low volume = less liquid.
- **Beta**: Volatility relative to market. Beta > 1 = more volatile.

## Best Practices

1. **Always include disclaimers**: "This is not financial advice."
2. **Verify current data**: Stock prices change constantly
3. **Check multiple sources**: Don't rely on just one data source
4. **Understand the business**: Read company descriptions and news
5. **Look at trends**: Don't just check today's price - look at historical data
6. **Check for risks**: Look at beta, debt, and competition

## Example Analysis

```python
import yfinance as yf

def analyze_stock(symbol):
    ticker = yf.Ticker(symbol)
    info = ticker.info
    
    print(f"=== {info.get('longName', symbol)} ({symbol}) ===")
    print(f"Price: ${info.get('currentPrice')}")
    print(f"P/E: {info.get('trailingPE')}")
    print(f"Mkt Cap: ${info.get('marketCap', 0) / 1e9:.1f}B")
    print(f"Dividend: {info.get('dividendYield', 0) * 100:.2f}%")
    print(f"52W High/Low: ${info.get('fiftyTwoWeekHigh')}/${info.get('fiftyTwoWeekLow')}")
    print(f"Volume: {info.get('volume'):,}")
    print(f"Sector: {info.get('sector')}")
    
# Usage
analyze_stock("AAPL")
```

## Warning

**NOT FINANCIAL ADVICE**: The information provided by this skill is for educational and research purposes only. It should not be construed as financial advice, investment recommendations, or offers to buy/sell any securities.

Always:
- Do your own research
- Consult with a licensed financial advisor
- Consider your own risk tolerance
- Diversify your investments
- Never invest more than you can afford to lose
