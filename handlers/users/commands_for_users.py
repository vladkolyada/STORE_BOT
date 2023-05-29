from aiogram import types
import random
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp
from keyboards.default.first_keyboards import get_contact
from aiogram.utils.exceptions import MessageTextIsEmpty

from utils.misc.throttling import rate_limit
from loader import dp

basket = ["Apple", "Potato", "Tomato"]


@rate_limit(limit=5, key='/start')
@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    random_greetings = random.choice(['Hello.', 'Hi!', 'Welcome'])  # Why not?
    await message.answer(text=f'{random_greetings}\n\n '
                              f'For the first step, I need to get your phone number for your future orders.',
                         reply_markup=get_contact)


@dp.message_handler(CommandHelp())
async def help_command(message: types.Message):
    await message.answer(text='help')


@dp.message_handler(commands='basket')
async def basket_command(message: types.Message):
    try:
        await message.answer(text='\n\n'.join(basket))
    except MessageTextIsEmpty:
        await message.answer(text='The basket is clean. Put your products here.')



