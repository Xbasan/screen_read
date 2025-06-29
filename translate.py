import requests
from API_K import TRANSLATE_API_KEY as API_KEY
from API_K import folder_id

URL = "https://translate.api.cloud.yandex.net/translate/v2/translate"
G_URL = "https://translate.googleapis.com/translate_a/single?client=gtx&"
target_language = "ru"


headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key {0}".format(API_KEY),
}


def g_translate(texts: list, language="ru") -> str:
    """
        Делает перивод текста через Google Translate
    """
    url = f"{G_URL}sl=auto&tl={language}&dt=t&q={"+".join(texts)}"
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
        response = requests.post(URL, json=body, headers=headers)
    except requests.exceptions.ConnectionError:
        return "Вайнах телеком снова инет отрубил"

    if response.status_code == 200:
        response_json = response.json()
        return [t['text'] for t in response_json.get('translations', [])]
    else:
        return ["Translate Eror"]
