from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage



storage = MemoryStorage()


token = config("token")
bot = Bot(token)
dp = Dispatcher(bot=bot, storage=storage)
