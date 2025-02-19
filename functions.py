import requests
from bs4 import BeautifulSoup


def num_to_text(num: int, s: int):
    text = ""
    if num == 0:
        text += 'ноль'
    if num == 1:
        if 0 <= s <= 1:
            text += 'один'
        else:
            text += 'одна'
    elif num == 2:
        if 0 <= s <= 1:
            text += 'два'
        else:
            text += 'две'
    elif num == 3:
        text += 'три'
    elif num == 4:
        text += 'четыре'
    elif num == 5:
        text += 'пять'
    elif num == 6:
        text += 'шесть'
    elif num == 7:
        text += 'семь'
    elif num == 8:
        text += 'восемь'
    elif num == 9:
        text += 'девять'
    elif num == 10:
        text += 'десять'
    elif num == 11:
        text += 'одиннадцать'
    elif num == 12:
        text += 'двенадцать'
    elif num == 13:
        text += 'тринадцать'
    elif num == 14:
        text += 'четырнадцать'
    elif num == 15:
        text += 'пятнадцать'
    elif num == 16:
        text += 'шестнадцать'
    elif num == 17:
        text += 'семнадцать'
    elif num == 18:
        text += 'восемнадцать'
    elif num == 19:
        text += 'девятнадцать'
    elif num == 20:
        text += 'двадцать'
    elif num // 10 == 2:
        text += 'двадцать ' + num_to_text(num % 10, 0)
    elif num == 30:
        text += 'тридцать '
    elif num // 10 == 3:
        text += 'тридцать ' + num_to_text(num % 10, 0)
    elif num == 40:
        text += 'сорок '
    elif num // 10 == 4:
        text += 'сорок ' + num_to_text(num % 10, 0)
    elif num == 50:
        text += 'пятьдесят '
    elif num // 10 == 5:
        text += 'пятьдесят ' + num_to_text(num % 10, 0)

    if s == 1:
        if num != 11 and num % 10 == 1:
            text += ' час'
        elif 2 <= num % 10 <= 4 and num // 10 != 1:
            text += ' часа'
        else:
            text += ' часов'
    elif s == 2:
        if num != 11 and num % 10 == 1:
            text += ' минута'
        elif 2 <= num % 10 <= 4 and num // 10 != 1:
            text += ' минуты'
        else:
            text += ' минут'

    return text


def what_weather(city):
    url = f"https://rp5.ru/Погода_в_{city}и,_{city}ская_область"
    class_ = "t_0"

    r = requests.get(url)
    html = BeautifulSoup(r.text, "html.parser")
    t = html.find(class_=class_).text
    n = int(t[1:-3])
    if n != 11 and n % 10 == 1:
        text = 'градус'
    elif 2 <= n % 10 <= 4 and n // 10 != 1:
        text = 'градуса'
    else:
        text = 'градусов'
    if t[0] == "+":
        t = f"плюс {num_to_text(n, 0)} {text}"
    else:
        t = f"минус {num_to_text(n, 0)} {text}"

    return t

