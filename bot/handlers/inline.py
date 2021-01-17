from aiogram.dispatcher.storage import FSMContext
from states import EditAd
from aiogram.types.force_reply import ForceReply
from keyboards.reply import choose_menu
from strings import SENDEDTOADMIN
from keyboards.inline import actions
from config import CHANNEL, GROUP
from aiogram import types
from loader import dp


@dp.callback_query_handler(text_startswith="ad")
async def func(query: types.CallbackQuery):
    action = query.data.split("_")[1]
    # await query.answer()
    await query.message.edit_reply_markup()
    if action == "confirm":
        await query.message.copy_to(GROUP, reply_markup=actions())
        await query.answer("So'rov adminga yuborildi")
        await query.message.answer(SENDEDTOADMIN, reply_markup=choose_menu())
    elif action == "cancel":
        await query.answer("Bekor qilindi")
        await query.message.edit_reply_markup()
    elif action == "delete":
        await query.answer("O'chirildi")
        await query.message.delete()
    elif action == "send":
        await query.message.copy_to(CHANNEL)
        await query.answer("E'lon kanalga tashlandi", show_alert=True)
    elif action == "edit":
        await query.message.reply("O'zgartirilgan e'lonni yuboring:", reply_markup=ForceReply())
        await EditAd.ad.set()

@dp.message_handler(state=EditAd.ad)
async def edit_ad(message: types.Message, state: FSMContext):
    ad = message.text
    await message.reply(ad, reply_markup=actions())
    await state.finish()