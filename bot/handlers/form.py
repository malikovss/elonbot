from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp
from strings import FORMS, MENUS, STATES, STATE_NAMES, TAG, TEXT, TITLE
from keyboards.reply import cancel_keyboard, choose_menu
from keyboards.inline import confirm
from states import Education, NeedEmployee, NeedEmployeeForSchool, NeedJob, NeedStudent, NeedTeacher


@dp.message_handler(text=MENUS+["Xоdim kerak",])
async def need_teacher(message: types.Message):
    await message.answer(TEXT.format(type=message.text.replace(" kerak","")))
    State = STATES[message.text]
    state_name = (await State.first()).split(":")[1]
    form = FORMS[message.text][state_name]
    text = form[0]+form[1]
    await message.answer(text, reply_markup=cancel_keyboard())


@dp.message_handler(state=[NeedEmployee, NeedTeacher, NeedStudent, Education, NeedJob, NeedEmployeeForSchool])
async def form(message: types.Message, state: FSMContext):
    state_class_name, state_name = (await state.get_state()).split(":")
    await state.update_data({f"{state_name}":message.text})
    State = STATES[STATE_NAMES[state_class_name]]
    form = FORMS[STATE_NAMES[state_class_name]]
    state_name = (await State.next())
    if state_name:
        state_name= state_name.split(":")[1]
        if state_name == "telegram":
            if message.from_user.username: username=message.from_user.username
            else: username=""
            await state.update_data(telegram=f"@{username}")
            state_name = (await State.next()).split(":")[1]
        text=form[state_name]
        await message.answer(text[0]+text[1])
    else:
        text = TITLE[STATE_NAMES[state_class_name]]+"\n\n"
        data = await state.get_data()
        for i in data:
            text+=f"{form[i][0]} {data[i]}\n"
        await message.answer(text+"\n"+TAG[STATE_NAMES[state_class_name]]+"\n\n➡️ @Talim_link kanaliga ulanish", reply_markup=confirm())
        await message.answer("Ma'lumotlar to'g'riligini tasdiqlang",reply_markup=choose_menu())
        await state.finish()
