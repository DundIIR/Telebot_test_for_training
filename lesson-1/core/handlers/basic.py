from aiogram import Bot
from aiogram.types import Message
from ..keyboards.reply import reply_keyboard, loc_tel_poll_keyboard
from ..keyboards.inline import select_macbook, get_inline_keyboard


async def get_inline(message: Message, bot: Bot):
    await message.answer(f'Привет, {message.from_user.first_name}. Вот клавиатура!',
                         reply_markup=get_inline_keyboard())

async def get_start(message: Message, bot: Bot):
    # await bot.send_message(message.from_user.id, f'<s>Привет {message.from_user.first_name}. Рад тебя видеть!</s>')
    # await message.reply(f'<tg-spoiler>Привет {message.from_user.first_name}. Рад тебя видеть!</tg-spoiler>')
    await message.answer(f'Привет <b>{message.from_user.first_name}</b>. Рад тебя видеть!',
                         reply_markup=loc_tel_poll_keyboard)

async def get_location(message: Message, bot: Bot):
    await message.answer(f'Ты отправил локацию!\r\a'
                         f'{message.location.latitude}\r\n{message.location.longitude}')

async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отлично, сохраню ее себе!')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')
