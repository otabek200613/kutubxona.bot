from aiogram.dispatcher.filters.state import State, StatesGroup

# Wikipedia qidiruv rejimi uchun state
class WikiState(StatesGroup):
    searching = State()