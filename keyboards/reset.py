from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_inline_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Сброс диалога", callback_data="reset")]
    ])
    return keyboard
