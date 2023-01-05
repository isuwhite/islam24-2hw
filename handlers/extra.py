from aiogram import types, Dispatcher
from config import bot, dp


@dp.message_handler()
async def echo(message: types.Message):
    try:
        await message.text.isdigit ** 2
    except:
        await message.answer(message.text)


async def dice_game():
    message.answer(dice_game())


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)