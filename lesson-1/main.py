from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from core.filters.iscontact import IsTrueContact
from core.handlers.basic import get_start, get_photo, get_location, get_inline
from core.handlers.contact import get_fake_contact, get_true_contact
from core.settings import settings
from core.keyboards.commands import set_commands
from core.handlers.callback import select_macbook, select_macbook_m2
from core.keyboards.callbackdata import MacInfo

import asyncio
import logging


async def start_bot(bot: Bot):
    await set_commands(bot)
    # await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    pass
    # await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_inline, Command(commands='inline'))
    dp.message.register(get_fake_contact, F.contact, IsTrueContact())
    dp.message.register(get_true_contact, F.contact)
    dp.callback_query.register(select_macbook, MacInfo.filter(F.processor != 'm2'))
    dp.callback_query.register(select_macbook_m2,  MacInfo.filter())
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_location, F.location)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
