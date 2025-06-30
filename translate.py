import requests
from API_K import TRANSLATE_API_KEY, folder_id
from url import Y_TRANSLATE_URL, G_TRANSLATE_URL

target_language = "ru"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key {0}".format(TRANSLATE_API_KEY),
}


def g_translate(texts: list, language="ru") -> str:
    """
        Делает перивод текста через Google Translate
    """
    url = f"{G_TRANSLATE_URL}sl=auto&tl={language}&dt=t&q={"+".join(texts)}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            res = response.json()
            return res[0][0][0]
        else:
            return response
    except requests.exceptions.Timeout:
        return "Привышена время ожидания"


def translate(texts: list) -> list:
    """
        Делает перивод текста через Yandex Translate
    """

    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }
    try:
        response = requests.post(Y_TRANSLATE_URL, json=body, headers=headers)
    except requests.exceptions.ConnectionError:
        return "Вайнах телеком снова инет отрубил"

    if response.status_code == 200:
        response_json = response.json()
        return [t['text'] for t in response_json.get('translations', [])]
    else:
        return ["Translate Eror"]
