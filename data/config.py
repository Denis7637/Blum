# api id, hash
API_ID = 123
API_HASH = 'API_HASH'

REF_LINK = 'https://t.me/blum/app?startapp=ref_xiopAzdA0y'

DELAYS = {
    "RELOGIN": [5, 7],  # задержка после попытки входа в систему
    'ACCOUNT': [5, 15],  # задержка между подключениями к аккаунтам (чем больше аккаунтов, тем больше задержка)
    'PLAY': [5, 15],   # задержка между играми в секундах
    'ERROR_PLAY': [5, 8],    # задержка между ошибками в игре в секундах
    'CLAIM': [600, 1800],   # задержка в секундах перед получением баллов каждые 8 часов
    'GAME': [35, 37],  # задержка после начала игры
    'TASK_COMPLETE': [2, 3],  # задержка после завершения задачи
    'TASK_ACTION': [5, 10]  # задержка после начала выполнения задачи
}

# если нужно играть в игру True/False
PLAY_GAME = True

# баллы за каждую игру; максимум 280
POINTS = [240, 280]

# True - если нужно перемешивать задания, не перемешивать - False
SHUFFLE_TASKS = True

# черный список заданий
BLACKLIST_TASK = ['Join or create tribe', 'How to Analyze Crypto?']

PROXY = {
    "USE_PROXY_FROM_FILE": False,  # True - если использовать прокси из файла, False - если использовать прокси из accounts.json
    "PROXY_PATH": "data/proxy.txt",  # путь к файлу с прокси
    "TYPE": {
        "TG": "socks5",  # тип прокси для клиента Telegram. Поддерживаются "socks4", "socks5" и "http"
        "REQUESTS": "socks5"  # тип прокси для запросов. "http" для https и http прокси, "socks5" для socks5 прокси.
        }
}

# папка сессий (не изменять)
WORKDIR = "sessions/"

# таймаут в секундах для проверки аккаунтов на валидность
TIMEOUT = 30
