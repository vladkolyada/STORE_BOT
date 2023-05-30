from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Start the bot'),
            types.BotCommand('help', "Get all commands"),
            types.BotCommand('basket', "Check data of basket"
                                       "(works only after passing authorization by entering "
                                       "the /start command)")
        ]
    )
