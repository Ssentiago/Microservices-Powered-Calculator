from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

top_row = [InlineKeyboardButton(text=i, callback_data=i) for i in ['С']]
numbers = [InlineKeyboardButton(text=f"{i}", callback_data=f"{i}") for i in range(1, 10)]
numbers = [numbers[start: start + 3] for start in range(0, 9, 3)]
down_row = [InlineKeyboardButton(text=i, callback_data=i) for i in ['0', '.', '⌫']]
keyboard = [top_row, *numbers[::-1], down_row]
syms = iter([InlineKeyboardButton(text=i, callback_data=i) for i in ['÷', '×', '-', '+', '=']])

for elem in keyboard:
    elem.append(next(syms))

keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
