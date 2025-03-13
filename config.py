import os
from dotenv import load_dotenv

load_dotenv() 

class Config:
    """
    Класс для хранения конфигурационных данных, 
    загруженных из переменных окружения.

    Этот класс предоставляет доступ к настройкам,
    которые хранятся в файле `.env` или в переменных окружения.

    Атрибуты:
        BOT_TOKEN (str): токен для доступа к Telegram Bot API.
        Загружается из переменной окружения "BOT_TOKEN".

        OPENROUTER_API_KEY (str): API-ключ для доступа к сервису OpenRouter.
        Загружается из переменной окружения "OPENROUTER_API_KEY".

        CSV_PATH (str): путь к CSV-файлу, используемому в приложении.
        Загружается из переменной окружения "CSV_PATH".
    """
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    CSV_PATH = os.getenv("CSV_PATH")