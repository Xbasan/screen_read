"""
Функции для работы с Google Gemini AI
Содержит:
- gemini(text: str) -> list: обрабатывает текст через Google Gemini AI.
- gemini_image(im_b64, prompt="Что это") -> list: обрабатывает изображение
(в base64) через Google Gemini AI.
"""

from requests import post, exceptions
from API_K import GEMINI_API
from url import GEMEMI_URL_IMAGE, GEMINI_URL_TEXT

he = {
    "Content-Type": "application/json",
    "x-goog-api-key": GEMINI_API
}


def gemini(text: str) -> list:
    """
        Выполняет запросы к Gemini связанные с текстам
    """
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"ответь на русском\n{text}"
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
    try:
        response = post(GEMINI_URL_TEXT, json=payload, headers=he, timeout=20)

        res_text = (response.json()
                    .get("candidates")[0]
                    ["content"]
                    ["parts"][0]
                    ["text"])
        return res_text, response.json().get("responseId")
    except (exceptions.ConnectionError, exceptions.Timeout):
        return "Вайнах телеком снова инет отрубил", 1


def gemini_image(im_b64, prompt="Что это") -> list:
    """
        Выполняет запросы к Gemini связанные с изображения
    """
    payload = {
            "contents": [{
                "parts": [
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": f"{im_b64}"
                        }
                    },
                    {"text": f"ответь на русском\n{prompt}"},
                ]}
            ]
        }

    response = post(GEMEMI_URL_IMAGE, json=payload, headers=he)

    res_text = (response.json()
                .get("candidates")[0]
                ["content"]
                ["parts"][0]
                ["text"])

    return res_text, response.json().get("responseId")
