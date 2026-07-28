# Morning Macro Brief

A morning brief that pulls together markets, headlines and a quick AI summary to give an outlook on the day's events and their potential macro impacts.
It's a personal project and a work in progress.

## What it does

Fetches and displays:
- **Live market prices** including: FTSE 100, GBP/USD, Brent Crude, US 10yr Treasury Yield
- **Headlines** from BBC Business, the Financial Times, and the Bank of England
- **An AI-generated briefing** summarising the key developments and any implications for UK inflation or monetary policy

The AI summary runs locally and at no cost via [Ollama](https://ollama.com) (Llama 3.2)

## How to run it

**1. Clone the repo**
```bash
git clone https://github.com/westonheller/morning-macro-brief.git
cd morning-macro-brief
```

**2. Set up the environment**
```bash
conda create -n macro_brief python=3.11
conda activate macro_brief
pip install -r requirements.txt
```

**3. Install Ollama and pull the model**

Download from [ollama.com](https://ollama.com), then:
```bash
ollama pull llama3.2
```

**4. Run**
```bash
streamlit run app.py
```

## Limitations worth knowing

- The AI occasionally hallucinates specific figures like inflation rates or interest rates. It's a small local model, so I'd suggest sanity checking anything numerical (apart from the market prices).
- Market prices are Yahoo Finance closing prices so may lag slightly during market hours.
- UK gilt yields not yet included on the list (no obvious reliable source yet).

## Possible extensions

-Email delivery of the morning briefing
-Economic calendar for upcoming releases
-UK gilt yields and additional market indicators
-Historical archive of previous briefings
-Interactive charts and trend visualisations

## Author
Weston Heller | Linkedin: www.linkedin.com/in/weston-heller | Email: westonheller145@gmail.com
