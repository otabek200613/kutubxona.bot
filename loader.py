from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from middlewares.force_subscribe import ForceSubscribeMiddleware
from middlewares.throttling import ThrottlingMiddleware

bot = Bot(token="8309391948:AAFRq-oe0DYoT9b_1CTjv0I4TnIcgG8f5kI")
dp = Dispatcher(bot, storage=MemoryStorage())

# Middleware ulash
dp.middleware.setup(ForceSubscribeMiddleware(bot))
dp.middleware.setup(ThrottlingMiddleware())
