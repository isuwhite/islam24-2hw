from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from config import bot, dp


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Приветствую {message.from_user.first_name}")

async def help_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"/start - Запуск\n"
                                f"/help - Помошь\n"
                                f"/quiz - Викторина\n"
                                f"/mem - Мемчик\n"
                                f"/game - Игра")

#дз про мемы
async def mem_handler(message: types.Message):
    photo = open("media/пацаны.jpg", "rb")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
#дз про эмоджи
async def game_handler(message: types.Message):
    await message.reply_dice()

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Чему равняется число ПИ"
    answers = [
        "2.34",
        "3.13",
        "4.13",
        "1.14",
        "3.14",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="Иди учись",
        open_period=5,
        reply_markup=markup
    )




async def get_anime(message: types.Message):
    anime = parser()
    for i in anime:
        await message.answer(
            f"{i['link']}\n\n"
            f"{i['title']}\n"
            f"{i['status']}\n"
            f"#Y{i['date']}\n"
            f"#{i['country']}\n"
            f"#{i['genre']}\n"
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(help_handler, commands=['help'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(game_handler, commands=['game'])

