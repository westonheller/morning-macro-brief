import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": "Say hello in one short sentence.",
        "stream": False
    }
)

if response.status_code == 200:
    result = response.json()
    print("Ollama is working. Response:")
    print(result["response"])
else:
    print(f"Something went wrong. Status code: {response.status_code}")