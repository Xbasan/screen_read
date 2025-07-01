"""
Модуль для перевода текста с использованием Google Translate и Yandex Translate

Содержит функции:
- g_translate(texts: list, language): перевод текста через Google.
- y_translate(texts: list, language): перевод текста через Yandex.
"""

from requests import post, get, exceptions
from urllib.parse import quote

from API_K import TRANSLATE_API_KEY, folder_id
from url import Y_TRANSLATE_URL, G_TRANSLATE_URL

headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key {0}".format(TRANSLATE_API_KEY),
}


def g_translate(texts: list, language="ru") -> str:
    """
        Делает перивод текста через Google Translate
    """
    prompt = quote(" ".join(texts), safe="")
    url = f"{G_TRANSLATE_URL}sl=auto&tl={language}&dt=t&q={prompt}"
    try:
        response = get(url, timeout=10)
        if response.status_code == 200:
            res = response.json()
            return res[0][0][0]
        else:
            return response
    except exceptions.Timeout:
        return "Привышена время ожидания"


def y_translate(texts: list, language="ru") -> list:
    """
        Делает перивод текста через Yandex Translate
    """

    body = {
        "targetLanguageCode": language,
        "texts": texts,
        "folderId": folder_id,
    }
    try:
        response = post(Y_TRANSLATE_URL, json=body, headers=headers)
    except exceptions.ConnectionError:
        return "Вайнах телеком снова инет отрубил"

    if response.status_code == 200:
        response_json = response.json()
        return [t['text'] for t in response_json.get('translations', [])]
    else:
        return ["Translate Eror"]
