from aiogram import Bot, Dispatcher
from config import Config
from handlers import start, shopping
import asyncio

async def main():
    """
    Основная асинхронная функция, которая запускает бота и настраивает диспетчер.

    Эта функция выполняет следующие шаги:
    1. Создает экземпляр бота с использованием токена из конфигурации.
    2. Создает экземпляр диспетчера, который будет обрабатывать входящие сообщения.
    3. Регистрирует роутеры из модулей `start` и `shopping` в диспетчере.
    4. Запускает процесс опроса серверов Telegram для получения новых сообщений.
    """
    bot = Bot(token=Config.BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(shopping.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())