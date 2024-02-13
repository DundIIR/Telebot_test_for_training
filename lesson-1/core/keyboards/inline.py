from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from ..keyboards.callbackdata import MacInfo

select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Macbook 2001',
            callback_data='macbook_2001'
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook 2002',
            callback_data='macbook_2002'
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook 2002',
            callback_data='macbook_2002'
        )
    ],
    [
        InlineKeyboardButton(
            text='Link',
            url='https://www.youtube.com/watch?v=XJCYxIbsXmk&list=PLRU2Gs7fnCuiwcEDU0AWGkSTawEQpLFPb&index=6'
        )
    ]
])


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Macbook 2001', callback_data=MacInfo(name='macbook', year=2001, processor='i5'))
    keyboard_builder.button(text='Macbook 2002', callback_data=MacInfo(name='macbook', year=2002, processor='m1'))
    keyboard_builder.button(text='Macbook 2003', callback_data=MacInfo(name='macbook', year=2003, processor='m2'))

    keyboard_builder.adjust(2, 1)
    return keyboard_builder.as_markup()
