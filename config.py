import yaml

# Свойства ассистента
VA_NAME = 'Джарвис'
VA_VER = "0.0.1"
VA_TBR = ('скажи', 'покажи', 'ответь', 'произнеси', 'расскажи', 'сколько')

# Свойства пользователя
USER_NAME = "Макар"
USER_TOWN = "Тюмен"

# Пути к программам
YA_PATH = 'C:/Users/Daniil/AppData/Local/Yandex/YandexBrowser/Application/browser.exe %s'

# Команды
VA_CMD_LIST = yaml.safe_load(
    open('commands.yaml', 'rt', encoding='utf8'),
)