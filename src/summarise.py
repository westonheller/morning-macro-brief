import requests
from datetime import date

# Ollama runs locally on this port by default
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2"


def build_prompt(prices: dict, headlines: list) -> str:
    """
    Build prompt to send to Ollama.
    Take prices dictionary and headlines list from other modules
    and format into a clear briefing request
    """
    today = date.today().strftime("%A %d %B %Y")

    # Format prices into readable lines
    price_lines = "\n".join(
        f"  {name}: {value}" for name, value in prices.items()
    )

    # Format headlines into a numbered list
    headline_lines = "\n".join(
        f"  {i+1}. {item['title']} ({item['source']})"
        for i, item in enumerate(headlines)
    )

    prompt = f"""You are a macroeconomic analyst writing a short morning briefing for a UK economics student. Today's date is {today}.

Here are today's market prices:
{price_lines}

Here are today's top business headlines:
{headline_lines}

Write a short morning briefing (3-4 paragraphs) that:
- Summarises the most important economic developments
- Explains what matters most today and why
- Notes any implications for UK inflation, monetary policy, and the macroeconomy
- Is written clearly, like a note from an economist to a colleague

Do not repeat every headline. Focus on what is genuinely significant.
Do not sign off with a name or sign-off phrase. End with your final analytical point."""

    return prompt


def get_summary(prices: dict, headlines: list) -> str:
    """
    Send prices and headlines to Ollama and return the AI-generated briefing.
    """
    prompt = build_prompt(prices, headlines)

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
        }
    )

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Summary unavailable (Ollama returned status {response.status_code})"