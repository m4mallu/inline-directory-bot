#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : inline-directory-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/inine-directory-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3
import asyncio
import os
from pyrogram import Client
from presets import Presets
from library.sql import query_msg
from pyrogram.errors import FloodWait
from library.support import get_thumbnail, get_reply_markup
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQuery


if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config


# -------------------------- Answering Inline query --------------------------------- #
@Client.on_inline_query()
async def answer(bot, query: InlineQuery):
    id = query.from_user.id
    me = await Client.get_me(bot)
    try:
        member_status = await bot.get_chat_member(chat_id=Config.DEFAULT_CHAT_ROOM,
                                                  user_id=id
                                                  )
    except FloodWait as e:
        await asyncio.sleep(e.x)
    except Exception:
        return
    #
    results = []
    search = []
    string = query.query.strip()
    try:
        search = await query_msg(string)
    except FloodWait as e:
        await asyncio.sleep(e.x)
    for file in search:
        try:
            results.append(
                InlineQueryResultArticle(
                    title=file.name,
                    input_message_content=InputTextMessageContent(
                        Presets.RESULTS.format(f'{file.name}',
                                               f'{file.dept}'.upper(),
                                               f'{file.mobile}',
                                               f'{file.extension}',
                                               f'{file.mail}',
                                               f'{file.emp}')
                                               ),
                    description=f'{file.dept}'.upper(),
                    reply_markup=get_reply_markup(me.username),
                    thumb_url=await get_thumbnail(file)
                )
            )
        except Exception:
            pass
    #
    if results:
        try:
            switch_pm_text = Presets.RESULT_TXT
            await query.answer(
                results=results,
                is_personal=True,
                switch_pm_text=switch_pm_text,
                switch_pm_parameter="start"
            )
        except Exception:
            pass
    else:
        switch_pm_text = Presets.NO_RESULT_TXT
        if string:
            switch_pm_text = Presets.NO_RESULT_TXT_STR.format(string)
        try:
            await query.answer(
                results=[],
                switch_pm_text=switch_pm_text,
                switch_pm_parameter="okay"
            )
        except Exception:
            pass
