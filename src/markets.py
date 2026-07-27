import yfinance as yf

# Yahoo Finance ticker symbols for the assets we care about.
# Keeping this as a dictionary means we can change tickers or add new
# assets in one place, without touching the fetching logic itself.
TICKERS = {
    "FTSE100": "^FTSE",
    "GBP/USD": "GBPUSD=X",
    "Brent Crude": "BZ=F",
    "US 10yr Treasury Yield": "^TNX",  # placeholder - see note below
}


def get_price(ticker: str) -> float:
    """
    Fetch the most recent closing price for a given ticker symbol.
    """
    data = yf.Ticker(ticker)
    history = data.history(period="1d")
    latest_close = history["Close"].iloc[-1]
    return latest_close


def get_all_prices() -> dict:
    """
    Fetch the latest price for every asset in TICKERS.

    Returns:
        A dictionary mapping asset name -> latest price.
        e.g. {"FTSE100": 8234.5, "GBP/USD": 1.27, ...}
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