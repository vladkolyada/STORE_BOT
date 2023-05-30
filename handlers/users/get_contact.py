from aiogram import types

from loader import dp, db
from keyboards.inline.default_keyboard import fruits_or_vegetables
from states.steps import StatesForBot


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def getting_the_phone_number(message: types.Message):
    await StatesForBot.AfterAuthorization.set()
    await db.add_new_user_to_the_table(message.contact.user_id, message.contact.phone_number)
    await message.answer(text='Thanks for that!')
    await message.answer(text='Go shopping! Choose type of product.',
                         reply_markup=fruits_or_vegetables)
