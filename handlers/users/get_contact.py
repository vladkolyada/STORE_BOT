from aiogram import types

from loader import dp
from keyboards.default.first_keyboards import fruits_or_vegetables


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def getting_the_phone_number(message: types.Message):
    await message.answer(text='Thanks for that!')
    await message.answer(text='Go shopping! Choose type of product.',
                         reply_markup=fruits_or_vegetables)
