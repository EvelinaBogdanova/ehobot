import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "8126930606:AAFDVK3qZlreTnWCjm35ILweS_OuMrXe2F4"

HELP_TEXT = (
    "Команды:\n"
    "/start — запуск бота\n"
    "/help — помощь\n\n"
    "Просто напиши любой текст — я отвечу 🙂"
)

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def cmd_start(message: Message):
        await message.answer("Привет! Я эхо-бот.")
        await message.answer(HELP_TEXT)

    @dp.message(Command("help"))
    async def cmd_help(message: Message):
        await message.answer(HELP_TEXT)

    @dp.message(F.text)
    async def echo_text(message: Message):
        if not message.text.startswith('/'):
            await message.answer(f"Ты написал: {message.text}")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())