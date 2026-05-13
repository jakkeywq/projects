import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

print('[Bot] ТГ-бот працює...')


async def main():

    bot = Bot(token='7748594587:AAELGlprPiNrxZOCBBjwnladpctwDWW4P5w')
    dp = Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот вимкнений')