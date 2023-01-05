from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot

class fsm_admins(StatesGroup):
    ID = State()
    name = State()
    naprovlenie = State()
    age = State()
    group = State()
    submit = State()

async def start_fsm(message: types.Message):
    if message.chat.type == "private":
        await fsm_admins.ID.set()
        await message.answer("Введите своё ID")


    else:
        await message.answer("Личка!!!")

async def load_ID(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("only числа")
    else:
        async with state.proxy() as data:
            data["ID"] = message.text
        await fsm_admins.next()
        await message.answer("Как вас зовут?")

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await fsm_admins.next()
    await message.answer("Ваше напровление?")

async def load_naprovlenie(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["naprovlenie"] = message.text
    await fsm_admins.next()
    await message.answer("Сколько вам лет?")

async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Только числа!!!")
    else:
        async with state.proxy() as data:
            data["age"] = message.text
        await fsm_admins.next()
        await message.answer("Какая ваша группа?")

async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["group"] = message.text
        await message.answer(data['ID'],
                            f"{data['name']} {data['naprovlenie']} {data['age']} "
                            f"{data['group']}")

    await fsm_admins.next()
    await message.answer("Всё ли верно? Ответом может быть только да или нет")


async def load_submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await state.finish()
        await message.answer("Выполнено успешно!")
    elif message.text.lower() == "нет":
        await message.answer("Отменено")
        await state.finish()
    else:
         await message.answer("Только да или нет")



def register_handler_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(start_fsm, commands=["reg"])
    dp.register_message_handler(load_ID, state=fsm_admins.ID)
    dp.register_message_handler(load_name, state=fsm_admins.name)
    dp.register_message_handler(load_naprovlenie, state=fsm_admins.naprovlenie)
    dp.register_message_handler(load_age, state=fsm_admins.age)
    dp.register_message_handler(load_group, state=fsm_admins.group)
    dp.register_message_handler(load_submit, state=fsm_admins.submit)