from aiogram.dispatcher.filters.state import StatesGroup, State


class StatesForBot(StatesGroup):
    AfterAuthorization = State()
