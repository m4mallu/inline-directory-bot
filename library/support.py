#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : inline-directory-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/inine-directory-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3

import os
import asyncio
from presets import Presets
from urllib.parse import quote
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

chat_member = {}
user_name = {}

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config


# --------------------- Get thumbnail_url -------------------------------- #
async def get_thumbnail(file):
    thumb_nail = str()
    try:
        thumb = file.thumb_url
        thumb_nail = thumb if (thumb != "0") else Presets.THUMBNAIL_URL
    except FloodWait as e:
        await asyncio.sleep(e.x)
    return thumb_nail


# ---------------------------- reply markup share button --------------------- #
def get_reply_markup(username):
    url = 't.me/share/url?url=' + quote(Presets.SHARE_BUTTON_TEXT.format(username))
    buttons = [[InlineKeyboardButton('Share bot', url=url),
                InlineKeyboardButton("Search Here", switch_inline_query_current_chat='')]]
    reply_markup_share = InlineKeyboardMarkup(buttons)
    return reply_markup_share


# ----------- Filtering chat participants for inline query answer ------------ #
async def query_chat_participant(id, bot):
    # Saving the bot username for further usage
    if id not in user_name:
        try:
            me = await bot.get_me()
            user_name[id] = me.username
        except FloodWait as e:
            await asyncio.sleep(e.x)
    else:
        pass
    # Checking the queried user is a member of the default chat room.
    if id not in chat_member:
        try:
            member = await bot.get_chat_member(chat_id=Config.DEFAULT_CHAT_ROOM, user_id=id)
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception:
            return
        chat_member[id] = id
    else:
        pass

async def admin_info(bot):
    admins = []
    name = str()
    for names in Config.ADMIN_USERS:
        try:
            name = await bot.get_users(names)
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except Exception:
            pass
        if name:
            link = '🔰' + ' ' + name.mention()
            admins.append(link)
            name = str()
    return admins


async def map_chat_member(bot):
    user_ids = []
    async for users in bot.iter_chat_members(chat_id=Config.DEFAULT_CHAT_ROOM):
        member = await bot.get_chat_member(chat_id=Config.DEFAULT_CHAT_ROOM, user_id=users.user.id)
        user_ids.append(member.user.id)
    return user_ids
