import feedparser

# RSS feed URLs for news sources.
# Keeping these here means adding a new source later is just one new line.
FEEDS = {
    "BBC Business": "http://feeds.bbci.co.uk/news/business/rss.xml",
}

# How many headlines to pull from each feed.
MAX_HEADLINES = 10


def get_headlines(max_per_feed: int = MAX_HEADLINES) -> list:
    """
    Fetch the latest headlines from all feeds in FEEDS.

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

        for entry in feed.entries[:max_per_feed]:
            all_headlines.append({
                "source": source,
                "title": entry.title,
                "link": entry.link,
                "summary": entry.get("summary", "No summary available."),
            })

    return all_headlines


if __name__ == "__main__":
    headlines = get_headlines()
    for item in headlines:
        print(f"[{item['source']}] {item['title']}")
        print(f"  {item['link']}")
        print()