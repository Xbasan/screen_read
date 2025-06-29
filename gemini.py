import requests
from API_K import GEMINI_API

URL_IMAGE = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
URL_TEXT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

he = {
    "Content-Type": "application/json",
    "x-goog-api-key": GEMINI_API
}


def gemini(text: str) -> str:
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"{text}"
                    }
                ]
            }
        ],
        "generationConfig": {
            "thinkingConfig": {
                "thinkingBudget": 0
            }
        }
    }
    response = requests.post(URL_TEXT, json=payload, headers=he)

    res_text = (response.json()
                .get("candidates")[0]
                ["content"]
                ["parts"][0]
                ["text"])

    return res_text, response.json().get("responseId")
