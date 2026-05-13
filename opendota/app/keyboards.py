from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)



menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🔍 Проверка ID')],
    [KeyboardButton(text='🌊 Информация об аккаунте'), KeyboardButton(text='✏️ Изменить ID аккаунта')],
    ],

    resize_keyboard=True, 
    input_field_placeholder='Выберите пункт меню...'
    
)


cancelState = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='❌ Отмена', callback_data='cancelState')],
    
    ],
    
)

test = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='...')],
    [KeyboardButton(text='...')],

    ],
    resize_keyboard=True,
    input_field_placeholder='вавава'

)
