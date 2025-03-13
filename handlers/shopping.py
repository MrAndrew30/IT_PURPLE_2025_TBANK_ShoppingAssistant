from aiogram import Router, types
from aiogram.filters import Command
from shopping_assistant import ShoppingAssistant
from config import Config
from keyboards.reset import get_inline_keyboard

router = Router()
assistant = ShoppingAssistant(Config.CSV_PATH, Config.OPENROUTER_API_KEY)

@router.callback_query(lambda c: c.data == "reset")
async def reset_session(callback_query: types.CallbackQuery):
    """
    Обработчик команды /reset. Сбрасывает текущую сессию помощника.

    Когда пользователь отправляет команду /reset, текущая сессия помощника сбрасывается,
    и начинается новый диалог. Пользователь получает сообщение о том, что сессия сброшена.

    Аргументы:
        callback_query (types.CallbackQuery): информация о нажатой inline кнопке
    """
    await callback_query.answer()
    assistant.reset_session()
    await callback_query.message.answer("Сессия сброшена. Начинаем новый диалог.")

@router.message()
async def handle_message(message: types.Message):
    """
    Обработчик всех входящих сообщений

    Когда пользователь отправляет сообщение, оно передается помощнику для обработки.
    Полученный ответ отправляется обратно пользователю.

    Аргументы:
        message (types.Message): объект сообщения от пользователя.
    """
    user_message = message.text
    response = assistant.process_user_message(user_message)
    await message.answer(response, reply_markup=get_inline_keyboard())