from aiogram.filters.callback_data import CallbackData


class MacInfo(CallbackData, prefix='mac'):
    name: str
    year: int
    processor: str
