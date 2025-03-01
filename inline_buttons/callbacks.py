from start_bot import *

from aiogram import F
from manager.base import perfect_generate, short_description
from .buttons import *

@dp.callback_query(F.data == "regenerate_answer")
async def regenerate_button_callback(callback: types.CallbackQuery):
    await callback.message.edit_text("<i>Повторная генерация...</i>", parse_mode='HTML')
    answer = perfect_generate(manager.get_last_message()["text"],regenerate=True)
    desc = short_description(answer)
    try:
        await callback.message.edit_text(f"{answer}\n\n{'-' * 20}\n\n{desc}", reply_markup=regenerate_button())
    except:
        print(f"{answer}\n\n{'-' * 20}\n\n{desc}")