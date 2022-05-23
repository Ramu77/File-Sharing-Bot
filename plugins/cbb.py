#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Join : <code>@New_Telugu_Cinemas_bot ⚡</code>\n○ Contact Me : <a href='https://telegram.me/NewTeluguCinemas_bot'>Click here</a>\n○ New Telugu Cinemas : <a href='https://t.me/Mdisk_Telugu_Dubbed_Movies'>Click here</a>\n○ Channel : @New_Telugu_Cinemas_bot ⚡\n○ Support Me : @New_Telugu_Cinemas_bot ⚡</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
