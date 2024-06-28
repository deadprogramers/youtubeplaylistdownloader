# Copyright ©️ 2023 Sanila Ranatunga. All Rights Reserved

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔍Search YouTube", switch_inline_query_current_chat="")
        ]
    ]
)


@Client.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    reply_markup = START_BUTTONS
    await message.reply(
        f"Hello {message.from_user.first_name}!\n\nThis bot can search for YouTube videos & download YouTube videos, playlists and more. "
        f"To search videos click the below \"🔍Search Youtube\" button.\n\n"
        f"●/playlist_aud - <i>link</i> :-To download playlist videos in audio format\n"
        f"●/help :- For more info.", reply_markup=reply_markup)
