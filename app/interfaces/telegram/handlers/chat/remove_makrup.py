from aiogram import Router, F
from aiogram.types import ChatMemberUpdated, ReplyKeyboardRemove

from app.interfaces.telegram.messages import MESSAGES


router = Router()

@router.my_chat_member(
    F.new_chat_member.status.in_(["member", "administrator"])
)
async def bot_added(event: ChatMemberUpdated):
    language = event.from_user.language_code or "ru"
    if language not in ("ru", "en"):
        language = "ru"

    await event.bot.send_message(
        chat_id=event.chat.id,
        text=MESSAGES[language]["welcome_chat"],
        reply_markup=ReplyKeyboardRemove()
    )