from aiogram import types

from loader import dp, db
from keyboards.default.default_keyboards import remove_kb
from keyboards.inline.default_keyboard import fruits_or_vegetables
from states.steps import StatesForBot


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def getting_the_phone_number(message: types.Message):
    await StatesForBot.AfterAuthorization.set()
    await db.add_new_user_to_the_table(id=message.contact.user_id, phone_number=message.contact.phone_number,
                                       first_name=message.contact.first_name, last_name=message.contact.last_name)
    await message.answer(text='Thanks for that!', reply_markup=remove_kb)
    await message.answer(text='Go shopping! Choose type of product.',
                         reply_markup=fruits_or_vegetables)
