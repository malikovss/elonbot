from aiogram.dispatcher.filters.state import State, StatesGroup

class IsCorrect(StatesGroup):
    data = State()
    

class NeedEmployee(StatesGroup):
    center = State()
    subject = State()
    telegram = State()
    contact = State()
    address = State()
    responsible = State()
    working_hours = State()
    app_time = State()
    salary = State()
    addition = State()

class NeedTeacher(StatesGroup):
    student = State()
    age = State()
    subject = State()
    telegram = State()
    contact = State()
    address = State()
    price = State()
    job = State()
    app_time = State()
    target = State()

class NeedStudent(StatesGroup):
    teacher = State()
    age = State()
    subject = State()
    telegram = State()
    contact = State()
    address = State()
    price = State()
    job = State()
    app_time = State()
    target = State()


class Education(StatesGroup):
    center = State()
    address = State()
    subject = State()
    contact = State()
    telegram = State()
    price = State()
    payment = State()
    addition = State()


class NeedJob(StatesGroup):
    employee = State()
    age = State()
    subject = State()
    telegram = State()
    contact = State()
    address = State()
    job = State()
    app_time = State()
    target = State()
    addition = State()


class NeedEmployeeForSchool(StatesGroup):
    school = State()
    subject = State()
    telegram = State()
    contact = State()
    address = State()
    app_time = State()
    addition = State()


class EditAd(StatesGroup):
    ad = State()
