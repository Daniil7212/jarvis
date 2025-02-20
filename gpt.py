from mistralai import Mistral
import api

# from vosk_tts import Model, Synth
# model = Model(model_name="vosk-model-tts-ru-0.7-multi")
# synth = Synth(model)
#
# synth.synth("Привет мир!", "out.wav", speaker_id=2)

# Инициализация клиента
api_key = api.MISTRAL_API_KEY
client = Mistral(api_key=api_key)
embeds = []


def gpt_answer(request):
    # Подготовка сообщений
    messages = [
        {
            "role": "user",
            "content": f"{request} (ответь кратко)"
        }
    ]

    # Получение ответа
    chat_response = client.chat.complete(
        model="ministral-8b-latest",
        messages=messages
    )

    # Возврат ответа
    return chat_response.choices[0].message.content


# функция для разговора с gpt так чтобы он знал прошлые запросы
def gpt_embedded(request):
    embeds.append(request)
    embeddings_response = client.embeddings.create(
        model="mistral-embed",
        inputs=embeds,
    )

    return embeddings_response.choices[0].message.content


# print(gpt_answer("Привет, как дела"))
