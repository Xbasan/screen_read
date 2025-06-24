import requests
from API_K import TRANSLATE_API_KEY as API_KEY
from API_K import folder_id

URL = "https://translate.api.cloud.yandex.net/translate/v2/translate"
target_language = "ru"


headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key {0}".format(API_KEY),
}


def translate(texts: list) -> list:
    """
        Делает перивод текста
    """

    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }
    response = requests.post(URL, json=body, headers=headers)

    if response.status_code == 200:
        response_json = response.json()

        return [t['text'] for t in response_json.get('translations', [])]
    else:
        return ["Translate Eror"]
