from aiogram.types import (
     ReplyKeyboardMarkup
)
from strings import MENUS

def cancel_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Bekor qilish")
    return markup

def choose_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        "O'quv markaz",
        "Maktab"
    )
    return markup

def study_center_buttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        *MENUS
    )
    markup.add("◀️ Orqaga")
    return markup


def school_buttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        "Xоdim kerak"
    )
    markup.add("◀️ Orqaga")
    return markup

def is_correct():
    markup = ReplyKeyboardMarkup(row_width=2)
    markup.add(
        "Ha","Yo'q"
    )
    return markup