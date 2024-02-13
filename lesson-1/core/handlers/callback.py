from aiogram import Bot

from aiogram.types import CallbackQuery
from ..keyboards.callbackdata import MacInfo

# async def select_macbook(call: CallbackQuery, bot: Bot):
#     model = call.data.split('_')[0]
#     year = call.data.split('_')[1]
#     answer = f'{call.from_user.first_name}, ты выбрал Apple {model} {year}'
#     await call.message.answer(answer)
#     await call.answer()


async def select_macbook(call: CallbackQuery, bot: Bot, callback_data: MacInfo):
    name = callback_data.name
    processor = callback_data.processor
    year = callback_data.year
    answer = f'{call.from_user.first_name}, ты выбрал Apple {name} {processor} {year}'
    await call.message.answer(answer)
    await call.answer()


async def select_macbook_m2(call: CallbackQuery, bot: Bot, callback_data: MacInfo):
    name = callback_data.name
    processor = callback_data.processor
    year = callback_data.year
    answer = f'{call.from_user.first_name}, ты выбрал Apple {processor} {year}'
    await call.message.answer(answer)
    await call.answer()
