from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext



import app.keyboards as kb
import app.server as serv
import app.states as states

import asyncio



router = Router()

# ———————————————————————————————————————————————————————————

@router.message(CommandStart())
async def botStart(message:Message):

    await message.answer('🐳',
        reply_markup=kb.menu                     
    )

# ———————————————————————————————————————————————————————————

@router.message(F.text == '🐳 Інформація')
async def info(message: Message):
    await message.answer('Управління сервером через тг-бота',
        parse_mode='HTML'
    )


@router.message(F.text == '🗿 Команди')
async def commandList(message: Message):
    await message.answer('⭐️ Список команд... \n',
        parse_mode='HTML',
        reply_markup=kb.commands
    )


@router.message(F.text == '👤 Список гравців')
async def playerList(message: Message):
    plList = serv.checkList()

    await message.answer(plList,
        parse_mode='HTML'                    
    )

    
    


# ———————————————————————————————————————————————————————————


@router.callback_query(F.data == 'everyGlow')
async def everyGlow(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.delete()
    
    await callback.message.answer('🤩')
    await callback.message.answer('✅ Гравці <b>підсвічені!</b>',
        parse_mode='HTML'
    )

    serv.everyPlayerGlow()

@router.callback_query(F.data == 'commandKill')
async def commandKill(callback: CallbackQuery):
    await callback.answer('')

    await callback.message.edit_text('⚙️ Виберіть <b>опцію...</b>',
        parse_mode='HTML',
        reply_markup=kb.killKeyboard
    )


@router.callback_query(F.data == 'everyKill')
async def everyKill(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.delete()

    await callback.message.answer('🫠')
    await callback.message.answer('✅ Гравці <b>вбиті!</b>',
        parse_mode='HTML'
    )
    
    serv.everyPlayerKill()


@router.callback_query(F.data == 'randomKill')
async def randomKill(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.delete()

    await callback.message.answer('🤫')
    await callback.message.answer('✅ Випадкового гравця <b>вбито!</b>',
        parse_mode='HTML'
    )
    
    serv.playerKill('@r')



@router.callback_query(F.data == 'specialKill')
async def killPlayerGetNick(callback: CallbackQuery, state=FSMContext):
    await callback.answer('')

    await callback.message.edit_text('Введіть <b>нік</b> гравця!',
        parse_mode='HTML',
        reply_markup=kb.cancel
    )

    await state.set_state(states.KillOption.player_nickname)


@router.callback_query(F.data == 'cancelState')
async def cancelState(callback: CallbackQuery, state: FSMContext):

    await callback.answer('')
    await callback.message.delete()
    await state.clear()

# ———————————————————————————————————————————————————————————

@router.message(states.KillOption.player_nickname)
async def killPlayer(message: Message, state: FSMContext, callback=CallbackQuery):
    await state.update_data(player_nickname=message.text)

    data = await state.get_data()
    nickname = (data['player_nickname'])
    playerList = serv.checkRawList()

    if nickname in playerList:

        serv.playerKill(nickname)
        await message.answer('😵')
        await message.answer(f'✅ Гравця <b>{nickname}</b> вбито!',
            parse_mode='HTML'
        )
        await state.clear()
    
    else:
        msg = await message.answer('😓 Такого гравця <b>немає...</b>',
            parse_mode='HTML',   
        )
        await asyncio.sleep(3)
        await msg.delete()



# ———————————————————————————————————————————————————————————
