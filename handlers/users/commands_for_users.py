import random
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp

from keyboards.default.default_keyboards import get_contact
from utils.misc.throttling import rate_limit
from loader import dp
from states.steps import StatesForBot


@rate_limit(limit=5, key='/start')
@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    random_greetings = random.choice(['Hello.', 'Hi!', 'Welcome.'])  # Why not?
    await message.answer(text=f'{random_greetings}\n\n '
                              f'For the first step, I need to get your phone number for your future orders.',
                         reply_markup=get_contact)


@rate_limit(limit=5, key='/help')
@dp.message_handler(CommandHelp(), state=StatesForBot.AfterAuthorization)
async def help_command(message: types.Message):
    await message.answer(text='/start - Start the bot\n'
                              '/help - Get all commands\n'
                              '/basket - Check data of basket '
                              '(works only after passing authorization by entering the /start command)'
                         )

