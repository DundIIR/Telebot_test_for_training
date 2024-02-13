from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='О работе бота'
        ),
        BotCommand(
            command='talk',
            description='Поговорить'
        ),
        BotCommand(
            command='inline',
            description='Показать инлайн клавиатуру'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
