import yfinance as yf

# Yahoo Finance ticker symbols for relevent indicators
# Keep this as a dictionary to change tickers in future
TICKERS = {
    "FTSE100": "^FTSE",
    "GBP/USD": "GBPUSD=X",
    "Brent Crude": "BZ=F",
    "US 10yr Treasury Yield": "^TNX",  # placeholder - see note below
}


def get_price(ticker: str) -> float:
    """
    Fetch most recent closing price for a given ticker symbol
    """
    data = yf.Ticker(ticker)
    history = data.history(period="1d")
    latest_close = history["Close"].iloc[-1]
    return latest_close


def get_all_prices() -> dict:
    """
    Fetch latest price for every indicator in TICKERS

    Returns:
        A dictionary mapping indicator name -> latest price.
    """
    prices = {}
    for name, ticker in TICKERS.items():
        try:
            prices[name] = get_price(ticker)
        except Exception as error:
            print(f"Could not fetch {name} ({ticker}): {error}")
            prices[name] = None
    return prices


if __name__ == "__main__":
    all_prices = get_all_prices()
    for name, price in all_prices.items():
        print(f"{name}: {price}")