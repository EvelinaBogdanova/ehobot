import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

TOKEN = '8126930606:AAFDVK3qZlreTnWCjm35ILweS_OuMrXe2F4'
async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    @dp.message(F.text)

    async def echo_text(message: Message):
        await message.answer(message.text)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())