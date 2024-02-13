from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Ряд 1, кн 1'),
        KeyboardButton(text='Ряд 1, кн 2'),
        KeyboardButton(text='Ряд 1, кн 3')
    ],
    [
        KeyboardButton(text='Ряд 2, кн 1'),
        KeyboardButton(text='Ряд 2, кн 2'),
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выбери кнопку 👇', selective=True)

loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Отправить геолокацию', request_location=True)
    ],
    [
        KeyboardButton(text='Отправить контакт', request_contact=True)
    ],
    [
        KeyboardButton(text='Создать викторину', request_poll=KeyboardButtonPollType())
    ]

], resize_keyboard=True, one_time_keyboard=False)