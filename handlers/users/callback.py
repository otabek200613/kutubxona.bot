from aiogram import types
from loader import dp, bot
from utils.check_sub import check_subscription
from keyboards.default.buttons import start_button

@dp.callback_query_handler(text="check_sub")
async def check_sub_handler(call: types.CallbackQuery):
    user_id = call.from_user.id
    subscribed = await check_subscription(bot, user_id)

    if subscribed:
        await call.message.answer("✔ Rahmat! Endi botdan foydalanishingiz mumkin.",reply_markup=start_button)
        await call.message.delete()