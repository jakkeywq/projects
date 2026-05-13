import asyncio
import time
import random

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from mcrcon import MCRcon


api_token = '...'
rcon_ip = 'localhost'
rcon_port = 25575
rcon_password = '12345'

bot = Bot(token=api_token)
dp = Dispatcher()

cooldowns = {}
cooldown_time = 60

def command(cmd):
    try:
        with MCRcon(rcon_ip, rcon_password, port=rcon_port) as mcr:
            return mcr.command(cmd)
    except Exception as e:
        return f"Ошибка: {e}"

def checkNickname(nickname):
    return not nickname.startswith("@")

# ——————————————————————————————————————————————————————————————

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(":3")

# ——————————————————————————————————————————————————————————————

@dp.message(Command("players"))
async def list_players(message: types.Message):

    raw_response = command("list")
    

    if "online:" in raw_response:
        players_part = raw_response.split("online:")[1].strip()
        if not players_part:
            return await message.answer("👻 На сервере нету никого...")
        
        player_list = [p.strip() for p in players_part.split(",")]
        

        response_text = "<b>Игроки онлайн:</b>\n\n"
        for p in player_list:
            response_text += f"👤 <code>{p}</code>\n"
        
        await message.answer(response_text, parse_mode=ParseMode.HTML)
    else:
        await message.answer(f"Ответ сервера: {raw_response}")

# ——————————————————————————————————————————————————————————————

@dp.message(Command("kill"))
async def kill_player(message: types.Message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id in cooldowns and (current_time - cooldowns[user_id]) < cooldown_time:
        left = int(cooldown_time - (current_time - cooldowns[user_id]))
        return await message.answer(f"⏰ Подожди ещё {left} сек.")

    args = message.text.split()
    if len(args) < 2:
        return await message.answer("🚫 Напиши ник: /kill (...)", parse_mode=ParseMode.HTML)

    player = args[1]
    if not checkNickname(player):
        return await message.answer("❌ Селекторы запрещены!")

    command(f"kill {player}")
    cooldowns[user_id] = current_time
    await message.answer(f"💀 Игрок <code>{player}</code> был уничтожен!", parse_mode=ParseMode.HTML)

# ——————————————————————————————————————————————————————————————

@dp.message(Command("rtp"))
async def random_tp(message: types.Message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id in cooldowns and (current_time - cooldowns[user_id]) < cooldown_time:
        left = int(cooldown_time - (current_time - cooldowns[user_id]))
        return await message.answer(f"⏰ Подожди ещё {left} сек.")

    args = message.text.split()
    if len(args) < 2:
        return await message.answer("🚫 Напиши ник: /rtp (...)", 
                                    parse_mode=ParseMode.HTML)

    player = args[1]
    if not checkNickname(player):
        return await message.answer("❌ Селекторы запрещены!")
    
    rtp_icons = ["🔮", "✨", "⚡", "📍"]
    icon = random.choice(rtp_icons)

    command(f"execute at {player} run spreadplayers ~ ~ 0 100 false {player}")
    cooldowns[user_id] = current_time
    await message.answer(f"{icon} Игрок <code>{player}</code> переброшен!", 
                         parse_mode=ParseMode.HTML)

# ——————————————————————————————————————————————————————————————

@dp.message(Command("creeper"))
async def spawn_creeper(message: types.Message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id in cooldowns and (current_time - cooldowns[user_id]) < cooldown_time:
        left = int(cooldown_time - (current_time - cooldowns[user_id]))
        return await message.answer(f"⏰ Почекай ще {left} сек.")

    args = message.text.split()
    if len(args) < 2:
        return await message.answer("🚫 Напиши ник: /creeper (...)", parse_mode=ParseMode.HTML)

    player = args[1]
    if not checkNickname(player):
        return await message.answer("❌ Селектори заборонені!")
    
    cmd_creeper = f"execute at {player} run summon creeper ~ ~ ~ {{ExplosionRadius:0b, Fuse:30,ignited:1b}}"
    
    command(cmd_creeper)
    cooldowns[user_id] = current_time
    
    await message.answer(f"🧨 Сюрприз для <code>{player}</code> доставлен!", parse_mode=ParseMode.HTML)

# ——————————————————————————————————————————————————————————————

@dp.message(Command("levitation"))
async def levitation_all(message: types.Message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id in cooldowns and (current_time - cooldowns[user_id]) < cooldown_time:
        left = int(cooldown_time - (current_time - cooldowns[user_id]))
        return await message.answer(f"⏰ Подожди ещё {left} сек.")

    cmd_levitation = "effect give @a levitation 5 1 true"
    
    result = command(cmd_levitation)
    
    cooldowns[user_id] = current_time + 30
    
    await message.answer("🚀 <b>Все игроки отправлены в полет!</b>", parse_mode=ParseMode.HTML)

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
