from src.markets import get_all_prices
from src.news import get_headlines
from src.summarise import get_summary


def format_prices(prices: dict) -> str:
    """
    Format the prices dictionary into a readable block of text.
    """
    lines = []
    for name, value in prices.items():
        if value is None:
            lines.append(f"  {name}: unavailable")
        elif name == "US 10yr Treasury Yield":
            lines.append(f"  {name}: {value:.2f}%")
        elif name == "GBP/USD":
            lines.append(f"  {name}: {value:.4f}")
        else:
            lines.append(f"  {name}: {value:,.2f}")
    return "\n".join(lines)


def format_headlines(headlines: list) -> str:
    """
    Format the headlines list into a numbered block of text.
    """
    lines = []
    for i, item in enumerate(headlines):
        lines.append(f"  {i+1}. [{item['source']}] {item['title']}")
    return "\n".join(lines)


def run_brief():
    """
    Fetch all data, generate the AI summary, and print the morning brief.
    """
    print("=" * 60)
    print("        MORNING MACRO BRIEF")
    print("=" * 60)

    # --- Markets ---
    print("\nFetching market prices...")
    prices = get_all_prices()
    print("\nMARKETS")
    print("-" * 30)
    print(format_prices(prices))

    # --- Headlines ---
    print("\nFetching headlines...")
    headlines = get_headlines()
    print("\nHEADLINES")
    print("-" * 30)
    print(format_headlines(headlines))

    # --- AI Summary ---
    print("\nGenerating briefing (this may take 20-30 seconds)...")
    summary = get_summary(prices, headlines)
    print("\nAI BRIEFING")
    print("-" * 30)
    print(summary)

    print("\n" + "=" * 60)  