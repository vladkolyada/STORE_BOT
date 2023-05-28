from aiogram import types
import random
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp
from keyboards.default.first_keyboards import get_contact
from utils.misc.throttling import rate_limit
from handlers.users.functions_of_the_basket import basket

from loader import dp


@rate_limit(limit=5, key='/start')
# This is throttling. This helps for the quality work of the bot
# so that it doesn't slow down.
@dp.message_handler(CommandStart)
async def start_command(message: types.Message):
    random_greetings = random.choice(['Hello.', 'Hi!', 'Welcome'])  # Why not?
    await message.answer(text=f'{random_greetings}\n\n '
                              f'For the first step, I need to get your phone number for your future orders.',
                         reply_markup=get_contact)


@rate_limit(limit=5, key='/help')
@dp.message_handler(CommandHelp)
async def help_command(message: types.Message):
    pass


@rate_limit(limit=5, key='/basket')
@dp.message_handler(commands='/basket')
async def basket_command(message: types.Message):
    if basket is None:
        await message.answer(text='The basket is clean. Put your products here.')
    else:
        await message.answer(text='\n\n'.join(basket))



