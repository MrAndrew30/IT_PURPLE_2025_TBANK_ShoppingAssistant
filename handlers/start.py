from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message):
    """
    Обработчик команды start

    При первом входе в бота приветствует пользователя

    Аргументы:
        message (types.Message): объект сообщения от пользователя.
    """
    await message.answer("Добро пожаловать в Shopping Assistant! Чем могу помочь?")