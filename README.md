# Screen reader AI

Это приложение предоставляет удобный инструмент для захвата текста с экрана, его перевода и обработки с помощью искусственного интеллекта. Основные возможности:

[![Демо-видео](https://img.youtube.com/vi/qrER4tVXTiM/0.jpg)](https://youtu.be/qrER4tVXTiM)

- Захват выделенной области экрана;
- Распознавание текста с помощью OCR (EasyOCR);
- Перевод текста через сервис Google Translate или Yandex AI Translate;
- Анализ текста и изображения с помощью Gemini AI;
- Копирование результатов в буфер обмена.

```Shell
git clone https://github.com/Xbasan/screen_read
cd screen_read
pip install -r requirements.txt

python main_widget.py
```

Неоходиныме файлы это "API_K.py" имеюший следуюшее вид

- GEMINI_API - Главное API для работы функций свчзанных с AI
- TRANSLATE_API_KEY и folder_id - если хочешь использовать Yandex для перивода текста

```Python
TRANSLATE_API_KEY = "<Тут API-KEY от Yndex Translate>"
folder_id = "<ID директории Yndex Translate>"

GEMINI_API = "<Тут API-KEY из Google Ai Studio>"
```

