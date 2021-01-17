from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from aiogram.dispatcher import FSMContext
from keyboards.reply import choose_menu
from loader import dp


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='Bekor qilish', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("Bekor qilinadigan hech narsa yoq!", reply_markup=choose_menu())
        return
    await state.finish()
    await message.answer("Bekor qilindi!", reply_markup=choose_menu())