# Джарвис v1.0.0
import json
import config
import api
import time
import gpt
import sys
import struct
import vosk
import torch
import datetime
import webbrowser
import pvporcupine
import random
import playsound
import sounddevice as sd

from fuzzywuzzy import fuzz
from pvrecorder import PvRecorder
from functions import what_weather, num_to_text

# PORCUPINE
porcupine = pvporcupine.create(
    access_key=api.PORCUPINE_API_KEY,
    keywords=['jarvis'],
    sensitivities=[1]
)

recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
recorder.start()

# VOSK
model = vosk.Model("vosk_model_small")
samplerate = 16000
kaldi_rec = vosk.KaldiRecognizer(model, samplerate)

# Настройки модели
language = 'ru'
model_id = 'v4_ru'
sample_rate = 48000  # 48000
speaker = 'aidar'  # aidar, baya, kseniya, xenia, random
put_accent = True
put_yo = True
device = torch.device('cpu')  # cpu или gpu

# Организация модели
model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
model.to(device)


# Воспроизведение речи
def va_speak(what: str):
    audio = model.apply_tts(text=what,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)
    recorder.stop()
    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()
    print("Jarvis: " + what)
    recorder.start()


# Воспроизведение фраз
def play(sound: str):
    s: str = ""
    if sound == 'greet':
        r = str(random.randint(1, 3))
        s = f"C:/Users/Daniil/Desktop/Steve/sound/{sound + r}.wav"
    if sound == 'ok':
        r = str(random.randint(1, 3))
        s = f"sound/{sound + r}.wav"
    elif sound == 'not_found':
        s = f"sound/{sound}.wav"
    elif sound == 'off':
        s = f"C:/Users/Daniil/Desktop/Steve/sound/{sound}.wav"
    elif sound == 'ready':
        s = f"sound/{sound}.wav"
    elif sound == 'run':
        s = f"C:/Users/Daniil/Desktop/Steve/sound/{sound}.wav"
    elif sound == 'stupid':
        s = f"sound/{sound}.wav"
    elif sound == 'thanks':
        s = f"C:/Users/Daniil/Desktop/Steve/sound/{sound}.wav"

    playsound.playsound(s)


# Распознование речи
def va_respond(voice: str):
    print(voice)
    # обращаются к ассистенту
    if voice == '':
        return False
    cmd = recognize_cmd(voice)

    if cmd['cmd'] not in config.VA_CMD_LIST.keys():
        pass
    else:
        execute_cmd(cmd['cmd'], voice)
    return True


# Определение команды
def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


# Выполнение команды
def execute_cmd(cmd: str, voice: str):
    if cmd == 'help':
        # help
        text = "Я умею: ..."
        text += "произносить время ..."
        text += "открывать браузер и ютуб..."
        text += "и просто разговаривать"
        va_speak(text)
        pass
    elif cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        text = f"Сейчас {num_to_text(now.hour, 1)} {num_to_text(now.minute, 2)}"
        va_speak(text)
    elif cmd == 'hello':
        play("run")
    #  elif cmd == 'volume_off':
    #     text = f"Отключаю звук"
    #     tts.va_speak(text)
    #     devices = AudioUtilities.GetSpeakers()
    #     interface = devices.Activate(IAudioEndpointVolume.iid_, CLSCTX_ALL, None)
    #     volume = cast(interface, POINTER(IAudioEndpointVolume))
    #     volume.SetMute(1, None)
    # elif cmd == 'volume_on':
    #     text = f"Включааю звук"
    #     tts.va_speak(text)
    #     devices = AudioUtilities.GetSpeakers()
    #     interface = devices.Activate(IAudioEndpointVolume.iid_, CLSCTX_ALL, None)
    #     volume = cast(interface, POINTER(IAudioEndpointVolume))
    #     volume.SetMute(0, None)
    elif cmd == 'thanks':
        play("thanks")
    # elif cmd == 'music':
    #     text = f"Включаю!"
    #     va_speak(text)
    #     r = random.randint(0, 2)
    #     if r == 0:
    #         kostroma.start()
    #     elif r == 1:
    #         balamut.start()
    #     else:
    #         at_vinta.start()
    # elif cmd == 'music-off':
    #     text = f"Выключаю!"
    #     va_speak(text)
    #     kostroma.terminate()
    #     balamut.terminate()
    #     at_vinta.terminate()
    elif cmd == 'open_browser':
        webbrowser.get(config.YA_PATH).open("https://ya.ru/")
        play("ok")
    elif cmd == 'music':
        webbrowser.get(config.YA_PATH).open("https://music.yandex.ru/")
        play("ok")
    elif cmd == 'open_youtube':
        webbrowser.get(config.YA_PATH).open("https://www.youtube.com/")
        play("ok")
    elif cmd == 'recipes':
        webbrowser.get(config.YA_PATH).open("https://lavka.yandex.ru/recipes2")
        play("ok")
    elif cmd == 'cartoon':
        webbrowser.get(config.YA_PATH).open(
            "https://www.youtube.com/watch?v=YE2IL5kPZBo&list=PLeVA7eICJ6d2pgkb80PiilXDn88aMyzF6")
        play("ok")
    elif cmd == 'tell':
        gpt_answer = gpt.gpt_answer(voice)
        va_speak(gpt_answer)
        print("GPT: " + gpt_answer)
    elif cmd == 'google':
        webbrowser.get(config.YA_PATH).open("https://www.google.com/search?q=" + voice.split(' ', maxsplit=1)[1])
        play("ok")
    elif cmd == 'weather':
        weather = what_weather(config.USER_TOWN)
        va_speak(f'Температура на улице - {weather}')
    elif cmd == 'exit':
        play("off")
        sys.exit()


# Запуск
play("run")
print(f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")
ltc = time.time() - 1000

while True:
    try:
        pcm = recorder.read()
        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            recorder.stop()
            print("Yes, sir.")
            play("greet")
            recorder.start()
            ltc = time.time()

        while time.time() - ltc <= 8:
            pcm = recorder.read()
            sp = struct.pack("h" * len(pcm), *pcm)

            if kaldi_rec.AcceptWaveform(sp):
                if va_respond(json.loads(kaldi_rec.Result())["text"]):
                    ltc = time.time()
                break

    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise


bot.polling(none_stop=True)
print()
