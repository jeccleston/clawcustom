"""Stock analysis tool for clawcustom."""

import json
from typing import Any

try:
    import yfinance as yf

    YFINANCE_AVAILABLE = True
except ImportError:
    YFINANCE_AVAILABLE = False

from .tools.base import Tool


class StockAnalysisTool(Tool):
    """Tool for analyzing stocks and getting financial data."""

    @property
    def name(self) -> str:
        return "stock_analysis"

    @property
    def description(self) -> str:
        return "Get stock price, financial metrics, company info, and market data for any publicly traded company. Use this for investment research only."

    @property
    def parameters(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "Stock ticker symbol (e.g., AAPL, GOOGL, MSFT)",
                },
                "data_type": {
                    "type": "string",
                    "enum": ["price", "info", "history", "financials", "earnings", "news", "all"],
                    "description": "Type of data to retrieve",
                },
                "period": {
                    "type": "string",
                    "enum": ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "max"],
                    "description": "Historical period for price data",
                },
            },
            "required": ["symbol"],
        }

    async def execute(self, **kwargs: Any) -> str:
        if not YFINANCE_AVAILABLE:
            return "Error: yfinance not installed. Run: pip install yfinance"

        symbol = kwargs.get("symbol", "").upper().strip()
        data_type = kwargs.get("data_type", "all")
        period = kwargs.get("period", "1y")

        if not symbol:
            return "Error: Stock symbol is required"

        try:
            ticker = yf.Ticker(symbol)

            if data_type == "price" or data_type == "all":
                return self._get_price(ticker, symbol)
            elif data_type == "info":
                return self._get_info(ticker, symbol)
            elif data_type == "history":
                return self._get_history(ticker, symbol, period)
            elif data_type == "financials":
                return self._get_financials(ticker, symbol)
            elif data_type == "earnings":
                return self._get_earnings(ticker, symbol)
            elif data_type == "news":
                return self._get_news(ticker, symbol)
            else:
                return self._get_all(ticker, symbol, period)

        except Exception as e:
            return f"Error fetching data for {symbol}: {str(e)}"

    def _get_price(self, ticker: Any, symbol: str) -> str:
        info = ticker.info
        price = info.get("currentPrice")
        change = info.get("regularMarketChange")
        change_pct = info.get("regularMarketChangePercent")
        volume = info.get("volume")
        avg_volume = info.get("averageVolume")

        return json.dumps(
            {
                "symbol": symbol,
                "price": price,
                "change": change,
                "change_percent": change_pct,
                "volume": volume,
                "avg_volume": avg_volume,
                "market_cap": info.get("marketCap"),
            },
            indent=2,
        )

    def _get_info(self, ticker: Any, symbol: str) -> str:
        info = ticker.info
        data = {
            "symbol": symbol,
            "name": info.get("longName"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "ceo": info.get("ceo"),
            "employees": info.get("fullTimeEmployees"),
            "market_cap": info.get("marketCap"),
            "pe_ratio": info.get("trailingPE"),
            "forward_pe": info.get("forwardPE"),
            "dividend_yield": info.get("dividendYield"),
            "beta": info.get("beta"),
            "52_week_high": info.get("fiftyTwoWeekHigh"),
            "52_week_low": info.get("fiftyTwoWeekLow"),
            "volume": info.get("volume"),
            "avg_volume": info.get("averageVolume"),
            "description": info.get("longBusinessSummary", "")[:500],
        }
        return json.dumps(data, indent=2, default=str)

    def _get_history(self, ticker: Any, symbol: str, period: str) -> str:
        hist = ticker.history(period=period)
        if hist.empty:
            return f"No historical data for {symbol}"

        hist = hist.tail(30)
        data = {"symbol": symbol, "period": period, "data": []}
        for idx, row in hist.iterrows():
            data["data"].append(
                {
                    "date": idx.strftime("%Y-%m-%d"),
                    "open": round(row["Open"], 2),
                    "high": round(row["High"], 2),
                    "low": round(row["Low"], 2),
                    "close": round(row["Close"], 2),
                    "volume": int(row["Volume"]),
                }
            )
        return json.dumps(data, indent=2, default=str)

    def _get_financials(self, ticker: Any, symbol: str) -> str:
        try:
            income = ticker.income_stmt
            if income.empty:
                return f"No financial data for {symbol}"
            return income.to_json()
        except Exception as e:
            return f"Error fetching financials: {str(e)}"

    def _get_earnings(self, ticker: Any, symbol: str) -> str:
        try:
            earnings = ticker.quarterly_earnings
            if earnings.empty:
                return f"No earnings data for {symbol}"
            return earnings.to_json()
        except Exception as e:
            return f"Error fetching earnings: {str(e)}"

    def _get_news(self, ticker: Any, symbol: str) -> str:
        news = ticker.news
        if not news:
            return f"No news for {symbol}"

        articles = []
        for item in news[:10]:
            articles.append(
                {
                    "title": item.get("title"),
                    "publisher": item.get("publisher"),
                    "link": item.get("link"),
                    "published": item.get("pubDate"),
                }
            )
        return json.dumps({"symbol": symbol, "news": articles}, indent=2, default=str)

    def _get_all(self, ticker: Any, symbol: str, period: str) -> str:
        info = ticker.info
        hist = ticker.history(period=period)

        result = {
            "symbol": symbol,
            "name": info.get("longName"),
            "price": info.get("currentPrice"),
            "change": info.get("regularMarketChange"),
            "change_percent": info.get("regularMarketChangePercent"),
            "market_cap": info.get("marketCap"),
            "pe_ratio": info.get("trailingPE"),
            "dividend_yield": info.get("dividendYield"),
            "52_week_high": info.get("fiftyTwoWeekHigh"),
            "52_week_low": info.get("fiftyTwoWeekLow"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "volume": info.get("volume"),
            "recent_prices": [],
        }

        if not hist.empty:
            recent = hist.tail(10)
            for idx, row in recent.iterrows():
                result["recent_prices"].append(
                    {
                        "date": idx.strftime("%Y-%m-%d"),
                        "close": round(row["Close"], 2),
                    }
                )

        return json.dumps(result, indent=2, default=str)


class MarketOverviewTool(Tool):
    """Tool for getting market overview data."""

    @property
    def name(self) -> str:
        return "market_overview"

    @property
    def description(self) -> str:
        return "Get overview of major market indices (S&P 500, Dow, NASDAQ) and top movers."

    @property
    def parameters(self) -> str:
        return {
            "type": "object",
            "properties": {
                "indices": {
                    "type": "boolean",
                    "description": "Get major market indices",
                },
                "movers": {
                    "type": "boolean",
                    "description": "Get top gainers/losers",
                },
            },
        }

    async def execute(self, **kwargs: Any) -> str:
        if not YFINANCE_AVAILABLE:
            return "Error: yfinance not installed. Run: pip install yfinance"

        get_indices = kwargs.get("indices", True)
        get_movers = kwargs.get("movers", False)

        result = {}

        if get_indices:
            indices = {
                "S&P 500": "^GSPC",
                "Dow Jones": "^DJI",
                "NASDAQ": "^IXIC",
                "Russell 2000": "^RUT",
            }

            result["indices"] = {}
            for name, symbol in indices.items():
                try:
                    ticker = yf.Ticker(symbol)
                    info = ticker.info
                    result["indices"][name] = {
                        "price": info.get("currentPrice"),
                        "change": info.get("regularMarketChange"),
                        "change_percent": info.get("regularMarketChangePercent"),
                    }
                except:
                    pass

        if get_movers:
            popular = ["NVDA", "AMD", "TSLA", "META", "AMZN", "GOOGL", "AAPL", "MSFT"]
            result["movers"] = []
            for symbol in popular:
                try:
                    ticker = yf.Ticker(symbol)
                    info = ticker.info
                    result["movers"].append(
                        {
                            "symbol": symbol,
                            "price": info.get("currentPrice"),
                            "change": info.get("regularMarketChange"),
                            "change_percent": info.get("regularMarketChangePercent"),
                        }
                    )
                except:
                    pass

        return json.dumps(result, indent=2, default=str)


class CompareStocksTool(Tool):
    """Tool for comparing multiple stocks."""

    @property
    def name(self) -> str:
        return "compare_stocks"

    @property
    def description(self) -> str:
        return "Compare multiple stocks by price, performance, and key metrics."

    @property
    def parameters(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "symbols": {
                    "type": "string",
                    "description": "Comma-separated stock symbols (e.g., AAPL,GOOGL,MSFT)",
                },
                "period": {
                    "type": "string",
                    "enum": ["1d", "5d", "1mo", "3mo", "6mo", "1y"],
                    "description": "Period for performance comparison",
                },
            },
            "required": ["symbols"],
        }

    async def execute(self, **kwargs: Any) -> str:
        if not YFINANCE_AVAILABLE:
            return "Error: yfinance not installed. Run: pip install yfinance"

        symbols = [s.strip().upper() for s in kwargs.get("symbols", "").split(",")]
        period = kwargs.get("period", "1mo")

        if not symbols:
            return "Error: No symbols provided"

        try:
            data = yf.download(symbols, period=period)["Close"]

            result = {"comparison": []}
            for symbol in symbols:
                if symbol not in data.columns:
                    continue

                prices = data[symbol].dropna()
                if len(prices) < 2:
                    continue

                start_price = prices.iloc[0]
                end_price = prices.iloc[-1]
                change_pct = ((end_price / start_price) - 1) * 100

                ticker = yf.Ticker(symbol)
                info = ticker.info

                result["comparison"].append(
                    {
                        "symbol": symbol,
                        "name": info.get("longName"),
                        "current_price": round(end_price, 2),
                        "period_return": round(change_pct, 2),
                        "pe_ratio": info.get("trailingPE"),
                        "market_cap": info.get("marketCap"),
                        "dividend_yield": info.get("dividendYield"),
                    }
                )

            return json.dumps(result, indent=2, default=str)

        except Exception as e:
            return f"Error comparing stocks: {str(e)}"
