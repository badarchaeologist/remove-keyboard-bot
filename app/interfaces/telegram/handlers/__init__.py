from aiogram import Dispatcher

from .command.start import router as start_router
from .chat.remove_makrup import router as remove_router


def register_handlers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(remove_router) 
