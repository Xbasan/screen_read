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


class Gemini():
    def __init__(self):
        self.histori = {
            "contents": []
        }
        self.contents = []

    def update_histori(self, role: str, text: str) -> None:
        pass

    def gemini(self, text: str) -> list:
        """
            Выполняет запросы к Gemini связанные с текстам
        """

        self.contents.append({
                             "role": "user",
                             "parts": [
                                 {
                                     "text": text
                                 }
                             ]})

        payload = {
            "contents": self.contents,
            "generationConfig": {
                "thinkingConfig": {
                    "thinkingBudget": 0
                }
            }
        }
        try:
            response = post(GEMINI_URL_TEXT,
                            json=payload,
                            headers=he,
                            timeout=20)

            if response.status_code != 200:
                return f"Включич VPN {response.content()}"

            res_text = (response.json()
                        .get("candidates")[0]
                        ["content"]
                        ["parts"][0]
                        ["text"])

            self.contents.append({
                                 "role": "model",
                                 "parts": [
                                     {
                                         "text": res_text
                                     }
                                 ]})

            return res_text

        except (exceptions.ConnectionError, exceptions.Timeout):
            return "Вайнах телеком снова инет отрубил"

    def gemini_image(self, im_b64, prompt="Что это") -> str:
        """
            Выполняет запросы к Gemini связанные с изображения
        """

        self.contents.append({
                             "role": "user",
                             "parts": [
                                 {
                                     "inline_data": {
                                         "mime_type": "image/jpeg",
                                         "data": f"{im_b64}"
                                     }
                                 },
                                 {"text": f"ответь на русском\n{prompt}"},
                             ]})

        payload = {
                "contents": self.contents,
                "generationConfig": {
                    "thinkingConfig": {
                        "thinkingBudget": 0
                    }
                }}
        try:
            response = post(GEMEMI_URL_IMAGE,
                            json=payload,
                            headers=he,
                            timeout=30)

            if response.status_code != 200:
                return f"Включич VPN {response.json()}"

            res_text = (response.json()
                        .get("candidates")[0]
                        ["content"]
                        ["parts"][0]
                        ["text"])

            self.contents.append({
                                 "role": "model",
                                 "parts": [
                                     {
                                          "text": res_text
                                     }
                                 ]})

            return res_text

        except (exceptions.ConnectionError, exceptions.Timeout):
            print(response.content())
            return "Вайнах телеком снова инет отрубил"

