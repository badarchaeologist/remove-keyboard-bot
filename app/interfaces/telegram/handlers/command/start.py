from aiogram import Router, types, F
from aiogram.filters import CommandStart

from app.core.logger import logger
from app.interfaces.telegram.keyboards import inline 
from app.interfaces.telegram.messages import MESSAGES
from app.core.config import settings

router = Router()

@logger.catch
@router.message(CommandStart(), F.chat.type == "private")
async def start_handler(message: types.Message):
   
      language = message.from_user.language_code
      if language not in ("ru", "en"):
         language = "ru"

      await message.answer(
         MESSAGES[language]["welcome_private"],
         reply_markup=inline.start(settings.link, language)
      )
    