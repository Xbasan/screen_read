"""
Функции для работы с Google Gemini AI
Содержит:
- gemini(text: str) -> list: обрабатывает текст через Google Gemini AI.
- gemini_image(im_b64, prompt="Что это") -> list: обрабатывает изображение
(в base64) через Google Gemini AI.
"""

import asyncio
import qasync
from typing import AnyStr
import aiohttp
from requests import post, exceptions
from API_K import GEMINI_API
from url import GEMEMI_URL_IMAGE, GEMINI_URL_TEXT

he = {
    "Content-Type": "application/json",
    "x-goog-api-key": GEMINI_API
}

class Gemini():
    histori = {
            "contents": []
        }
    contents = []

    @staticmethod
    async def gemini_text(text: str) -> list:
        """
            Makes requests to Gemini related to texts
        """

        Gemini.contents.append({
                             "role": "user",
                             "parts": [
                                 {
                                     "text": text
                                 }
                             ]})

        payload = {
            "contents": Gemini.contents,
            "generationConfig": {
                "thinkingConfig": {
                    "thinkingBudget": 0
                }
            }
        }

        timeout = aiohttp.ClientTimeout(total=20)

        async with aiohttp.ClientSession(timeout=timeout) as session:
            try:
                async with session.post(GEMINI_URL_TEXT,
                                        json=payload,
                                        headers=he
                                    ) as resp:
                    if resp.status == 200:
                        res = await resp.json()

                        res_text = (res["candidates"][0]["content"]["parts"][0]["text"])                        
                         
                        Gemini.contents.append({
                                 "role": "model",
                                 "parts": [
                                     {
                                         "text": res_text
                                     }
                                 ]})
                        return res_text
                    else:
                        return ["Вайнах телеком снова инет отрубил", resp.content]
            except asyncio.TimeoutError:
                return ["Вайнах телеком снова инет отрубил"]


    @staticmethod
    async def gemini_image(im_b64, prompt="Что это") -> list:
        """
            Makes requests to Gemini related images
        """

        Gemini.contents.append({
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
                "contents": Gemini.contents,
                "generationConfig": {
                    "thinkingConfig": {
                        "thinkingBudget": 0
                    }
                }}


        timeout = aiohttp.ClientTimeout(total=30)

        async with aiohttp.ClientSession(timeout=timeout) as session:
            try:
                async with session.post(GEMEMI_URL_IMAGE,
                                        json=payload,
                                        headers=he
                                    ) as resp:
                    if resp.status == 200:
                        res = await resp.json()

                        res_text = (res["candidates"][0]["content"]["parts"][0]["text"])                        
                         
                        Gemini.contents.append({
                                 "role": "model",
                                 "parts": [
                                     {
                                         "text": res_text
                                     }
                                 ]})
                        return res_text
                    else:
                        return ["Вайнах телеком снова инет отрубил", resp.content]
            except asyncio.TimeoutError:
                return ["Вайнах телеком снова инет отрубил", "11"]

