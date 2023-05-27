import logging

from loader import dp
from data.config import ADMINS


async def on_startup_notify():
    for admin in ADMINS:
        try:
            await dp.bot.send_message(chat_id=admin, text="Bot is started")
        except Exception as err:
            logging.exception(err)
