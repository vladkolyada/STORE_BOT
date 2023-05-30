from aiogram import types

from loader import dp
from states.steps import StatesForBot
from keyboards.inline.fruits.fruit_selection import type_of_fruits


@dp.callback_query_handler(state=StatesForBot.AfterAuthorization)
async def fruit_or_vegetables(callback: types.CallbackQuery):
    if callback.data == 'fruits':
        await callback.message.edit_text(text='Choose type of fruit.',
                                         reply_markup=type_of_fruits)
