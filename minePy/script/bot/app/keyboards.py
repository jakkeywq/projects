from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)



menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🐳 Інформація')],
    [KeyboardButton(text='🗿 Команди'), KeyboardButton(text='👤 Список гравців')],
    ],

    resize_keyboard=True, 
    input_field_placeholder='Виберіть пункт меню...'
    
)


commands = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🌤 Підсвітити гравців', callback_data='everyGlow')],
    [InlineKeyboardButton(text='💀 Вбити гравців', callback_data='commandKill')],
    
    ],
    
)

killKeyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='👥 Вбити всіх', callback_data='everyKill')],
    [InlineKeyboardButton(text='🎲 Вбити випадкового гравця', callback_data='randomKill')],
    [InlineKeyboardButton(text='✏️ Вбити конкретного гравця...', callback_data='specialKill')],
    
    
    ],
    
)

cancel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🚫 Скасувати', callback_data='cancelState')]
    ],

)

test = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='...')],
    [KeyboardButton(text='...')],

    ],
    resize_keyboard=True,
    input_field_placeholder='вавава'

)


