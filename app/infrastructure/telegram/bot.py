from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramForbiddenError

from app.core.config import settings
from app.core.logger import logger
from app.interfaces.telegram.handlers import register_handlers
from app.interfaces.telegram.middlewares.error_handler import (
    ErrorHandlerMiddleware,
)


bot = Bot(
    token=settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())

dp.message.middleware(ErrorHandlerMiddleware())
dp.callback_query.middleware(ErrorHandlerMiddleware())


@dp.errors()
async def errors_handler(update, exception):
    if isinstance(exception, TelegramForbiddenError):
        logger.warning(f"Bot was blocked by user: {exception}")
        return
    logger.error(f"Unhandled exception: {exception}")

@logger.catch
async def main():
    logger.info("Starting bot...")

    register_handlers(dp)

    await dp.start_polling(bot)