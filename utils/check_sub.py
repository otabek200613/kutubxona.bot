from aiogram import Bot
from data.config import CHANNEL

async def check_subscription(bot: Bot, user_id: int):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        # Foydalanuvchi obuna bo‘lganmi tekshirish
        if member.status in ["member", "administrator", "creator"]:
            return True
        return False
    except Exception as e:
        print(f"Xatolik: {e}")
        return False