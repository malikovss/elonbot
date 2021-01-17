from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def confirm():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("✅ Tasdiqlash",callback_data='ad_confirm'),
        InlineKeyboardButton("❌ Bekor qilish", callback_data="ad_cancel"),
    )
    return markup

def actions():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("✅ Kanalga tashlash", callback_data="ad_send"),
        InlineKeyboardButton("🖋 O'zgartirish", callback_data="ad_edit"),
        InlineKeyboardButton("❌ O'chirish", callback_data="ad_delete"),
    )
    return markup