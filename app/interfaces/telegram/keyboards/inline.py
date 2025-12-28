from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, SwitchInlineQueryChosenChat

from app.interfaces.telegram.messages import BUTTONS

def start(link, language) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=BUTTONS[language]["developer"], 
                    url=link
                )
            ],
            [
                InlineKeyboardButton(
                    text=BUTTONS[language]["chat"],
                    switch_inline_query_chosen_chat=SwitchInlineQueryChosenChat(
                        query="",
                        allow_group_chats=True  
                    )
                )
            ]
        ]
    )