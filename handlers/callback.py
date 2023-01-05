from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import dp, bot



@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Кто самый умный?"
    answers = [
        "Meнделеев",
        "Энштейн",
        "Я",
        "Джобс",
    ]

    photo = open("media/Кошак.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation="да это так",

    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")