from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from utils.check_sub import check_subscription
# data.config faylidan kanallar ro'yxatini import qilamiz
# Agar sizda faqat bitta kanal bo'lsa ham, endi uni CHANNELS ro'yxatiga kiritish tavsiya etiladi.
# Masalan: CHANNELS = ["@Muhrbek_AI_bot_yordam", "@ona_tili_Muhrbek"]
from data.config import CHANNEL


class ForceSubscribeMiddleware(BaseMiddleware):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    async def on_pre_process_message(self, message: types.Message, data: dict):
        user_id = message.from_user.id
        # check_subscription funksiyasi barcha kanallarga obunani tekshirishi kerak
        subscribed = await check_subscription(self.bot, user_id)

        if not subscribed:
            keyboard = types.InlineKeyboardMarkup(row_width=1)

            # --- Dinamik tugmalar yaratish ---
            for channel_username in CHANNEL:
                # '@' belgisini o'chirib tashlaymiz
                username_without_at = channel_username.replace('@', '')

                # Har bir kanal uchun obuna tugmasini qo'shamiz
                keyboard.add(types.InlineKeyboardButton(
                    f"📢 Kanalga obuna bo‘lish ({channel_username})",
                    url=f"https://t.me/{username_without_at}"
                ))

            # --- Tekshirish tugmasi ---
            keyboard.add(types.InlineKeyboardButton(
                "🔄 Obunani tekshirish",
                callback_data="check_sub"
            ))

            # --- Xabar matni ---
            await message.answer(
                "🔒 Botdan foydalanish uchun talab qilingan **barcha kanallarga** obuna bo‘ling!",
                reply_markup=keyboard,
                parse_mode="Markdown"  # Matnni bold qilish uchun
            )
            # Obuna bo'lmagan bo'lsa, keyingi xandlerlarni bekor qiladi
            raise CancelHandler()

    async def on_pre_process_callback_query(self, call: types.CallbackQuery, data: dict):
        # Callback-ni bosgan foydalanuvchining ID-si
        user_id = call.from_user.id
        subscribed = await check_subscription(self.bot, user_id)

        if not subscribed:
            # Agar obuna bo'lmagan bo'lsa, xatolik xabarini chiqaradi
            await call.answer("❗ Siz hali barcha talab qilingan kanallarga obuna bo‘lmadingiz!", show_alert=True)
            # Callback so'rovini bekor qiladi
            raise CancelHandler()