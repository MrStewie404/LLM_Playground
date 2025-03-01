from aiogram.utils.keyboard import InlineKeyboardBuilder
from start_bot import types

def regenerate_button():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Сгенерировать повторно",
        callback_data="regenerate_answer")
    )
    return builder.as_markup()