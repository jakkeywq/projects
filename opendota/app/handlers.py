from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.filters.state import StateFilter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


import app.keyboards as kb
import dota
import app.states as states
import users

router = Router()

# ———————————————————————————————————————————————————————————

@router.message(CommandStart())
async def botStart(message:Message):

    await message.answer('🐣')
    await message.answer('yo',
        reply_markup=kb.menu
    )

# ———————————————————————————————————————————————————————————

@router.message(F.text == '🔍 Проверка ID', StateFilter(None))
async def checkID(message: Message):
    pass


@router.message(F.text == '🌊 Информация об аккаунте', StateFilter(None))
async def basic(message: Message):
    pass
            

# ———————————————————————————————————————————————————————————

@router.callback_query(F.data == 'cancelState')
async def cancelState(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await callback.message.delete()
    await state.clear()

# ———————————————————————————————————————————————————————————
