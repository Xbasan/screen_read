import requests
from API_K import GEMINI_API
from url import GEMEMI_URL_IMAGE, GEMINI_URL_TEXT

he = {
    "Content-Type": "application/json",
    "x-goog-api-key": GEMINI_API
}


def gemini(text: str) -> list:
    """
        Выполняет запросы к Gemini
    """
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
    response = requests.post(GEMINI_URL_TEXT, json=payload, headers=he)

    res_text = (response.json()
                .get("candidates")[0]
                ["content"]
                ["parts"][0]
                ["text"])

    return res_text, response.json().get("responseId")


def gemini_image(im_b64, prompt="Что это") -> list:
    payload = {
            "contents": [{
                "parts": [
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": f"{im_b64}"
                        }
                    },
                    {"text": f"{prompt}"},
                ]}
            ]
        }

    response = requests.post(GEMEMI_URL_IMAGE, payload, headers=he)

    res_text = (response.json()
                .get("candidates")[0]
                ["content"]
                ["parts"][0]
                ["text"])

    return res_text, response.json().get("responseId")
