# Jarvis v1.0.0

Jarvis - то небольшой голосовой ассистент с открытым исходным кодом, что позволяет дорабатывать его для своих нужд. В своей работе он использует нейросети Vosk, Porcupine, Silero TTS, Mistral AI.

## Содержание

- [Установка](#установка)
- [Использование](#использование)

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

## Возможности

- Просто поразговаривает (работает благодаря интеграции Mistral AI)
- Откроет бразуер или ютуб
- Скажет температуру на улице или время
