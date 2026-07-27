import feedparser

# RSS feed URLs for news sources.
# Keeping these here means adding a new source later is just one new line.
FEEDS = {
    "BBC Business": "http://feeds.bbci.co.uk/news/business/rss.xml",
    "FT": "https://news.google.com/rss/search?q=site:ft.com+economics&hl=en-GB&gl=GB&ceid=GB:en",
    "Bank of England": "https://www.bankofengland.co.uk/rss/news",
}

# How many headlines to pull from each feed.
MAX_HEADLINES = 5


def clean_title(title: str, source: str) -> str:
    """
    Remove source name suffixes that RSS feeds often append to titles.
    e.g. "Why surveys matter - Financial Times" -> "Why surveys matter"
    """
    suffixes = [
        " - Financial Times",
        " - FT",
        " | Financial Times",
    ]
    for suffix in suffixes:
        if title.endswith(suffix):
            title = title[:-len(suffix)]
    return title.strip()


def get_headlines(max_per_feed: int = MAX_HEADLINES) -> list:
    """
    Fetch the latest headlines from all feeds in FEEDS.
    Skips dud entries (too short or generic titles).

    Returns:
        A list of dictionaries, each containing:
        - 'source': the feed name (e.g. "BBC Business")
        - 'title': the headline
        - 'link': the URL to the full article
        - 'summary': a short description if available
    """
    all_headlines = []

    for source, url in FEEDS.items():
        feed = feedparser.parse(url)
        source_count = 0

        for entry in feed.entries[:max_per_feed + 5]:
            title = clean_title(entry.title, source)

            # Skip dud entries with generic or very short titles
            if len(title) < 15 or title in ["Home", "Financial Times", "Reuters", "Home - Financial Times"]:
                continue

            all_headlines.append({
                "source": source,
                "title": title,
                "link": entry.link,
                "summary": entry.get("summary", "No summary available."),
            })

            source_count += 1
            if source_count >= max_per_feed:
                break

    return all_headlines


if __name__ == "__main__":
    headlines = get_headlines()
    for item in headlines:
        print(f"[{item['source']}] {item['title']}")
        print(f"  {item['link']}")
        print()