# Jarvis v1.0.0

Jarvis - это небольшой голосовой ассистент с открытым исходным кодом, что позволяет дорабатывать его для своих нужд. В своей работе он использует нейросети Vosk, Porcupine, Silero TTS, Mistral AI.

## Содержание

- [Установка](#установка)
- [Стек](#стек)
- [Возможности](#возможности)

## Установка

Инструкции по установке и настройке проекта. Например:

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Daniil7212/jarvis.git
    ```
2. Откройте проект в IDE (Например: PyCharm или Visual Studio Code):
3. Создайте виртуальное окружение:
    ```bash
    python -m venv venv
    ```
4. Активируйте виртуальное окружение:
    - На Windows:
        ```bash
        venv\Scripts\activate
        ```
    - На macOS и Linux:
        ```bash
        source venv/bin/activate
        ```
5. Установите зависимости из файла `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
6. Установите модель для распознования речи "vosk-model-small-ru" [по ссылке](https://github.com/alphacep/vosk-space/blob/master/models.md) и поместите в папку с установленными исходниками.
7. Запустите проект:
    ```bash
    python main.py
    ```
   
## Стек

В проекте используется:
- [Python 3.12](https://www.python.org/) - основной язык программирования
- [yaml](https://ru.wikipedia.org/wiki/YAML) - язык сериализации для хранения списка команд
- [vosk](https://github.com/alphacep/vosk-space) - для распознавания речи
- [Picovoice Porcupine](https://console.picovoice.ai/ppn) - для Wake Word (активационной фразы)
- [silero-tts](https://github.com/snakers4/silero-models) - для синтеза речи
- [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/) - алгоритм расстояния Левенштейна
- [Mistral AI](https://mistral.ai/) - в качестве нейросети для разговора

## Возможности

- Просто поразговаривает (работает благодаря интеграции Mistral AI)
- Откроет бразуер или ютуб
- Скажет температуру на улице или время
