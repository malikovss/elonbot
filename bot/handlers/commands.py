from aiogram import types
from loader import dp
from keyboards.reply import choose_menu, study_center_buttons, school_buttons
from strings import START, HELP

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(START.format(name=message.from_user.first_name), reply_markup=choose_menu())


@dp.message_handler(commands="help")
async def help(message: types.Message):
    await message.answer(HELP)

@dp.message_handler(text="O'quv markaz")
async def study_center(message: types.Message):
    await message.answer("<b>Tanlang:</b>", reply_markup=study_center_buttons())


@dp.message_handler(text="Maktab")
async def school(message: types.Message):
    await message.answer("<b>Tanlang:</b>", reply_markup=school_buttons())


@dp.message_handler(text="◀️ Orqaga")
async def back(message: types.Message):
    await message.answer("Asosiy menyu:", reply_markup=choose_menu())