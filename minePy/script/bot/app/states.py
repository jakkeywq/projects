from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class KillOption(StatesGroup):
    player_nickname = State()

