from manager.base import perfect_generate, base_generate, short_description
import inline_buttons.buttons as inline_buttons
import inline_buttons.callbacks as inline_callbacks

from start_bot import *

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(base_generate("Привет!")[0])

@dp.message(Command("history"))
async def history_handler(message: Message):
    # Получаем и возвращаем обратное состояние памяти
    new_station = 'False' if manager.get_history() == True else 'True'
    manager.set_history(new_station)
    await message.answer(f"Память изменена на {new_station}")

@dp.message(Command("clear"))
async def clear_handler(message: Message):
    manager.set_memory()
    await message.answer(f"Память была очищена")

@dp.message(Command("info"))
async def info_handler(message: Message):
    memory = manager.get_memory()
    print(len(memory))
    history_status = '✅' if manager.get_history() else '❌'
    info = f"""Токенов в памяти: {len(memory)}\nИстория: {history_status}\n"""
    await message.answer(info)

@dp.message(Command("regenerate"))
async def regenerate_handler(message: Message):
    last_message = manager.get_last_message()
    answer = perfect_generate(last_message["text"], regenerate=True)
    desc = short_description(answer)
    await message.answer(f"{answer}\n\n{'-' * 20}\n\n{desc}")

@dp.message()
async def all_messages(message: Message):
    manager.set_last_message([message.message_id, message.text])
    answer = perfect_generate(message.text)
    await message.answer(answer, reply_markup=inline_buttons.regenerate_button())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())