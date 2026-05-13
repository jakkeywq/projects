from aiogram.fsm.state import State, StatesGroup

class ChangeID(StatesGroup):
    waiting_id = State()