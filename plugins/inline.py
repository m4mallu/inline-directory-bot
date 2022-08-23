#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : inline-directory-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/inine-directory-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3

import asyncio
from pyrogram import Client
from presets import Presets
from library.sql import query_msg
from library.support import chat_member, user_name
from library.support import get_thumbnail, get_reply_markup, query_chat_participant
from pyrogram.types import InputTextMessageContent, InlineQuery, InlineQueryResultPhoto


queried_user = {}


# -------------------------- Answering Inline query --------------------------------- #
@Client.on_inline_query()
async def answer(bot, query: InlineQuery):
    id = query.from_user.id
    results = []
    await query_chat_participant(id, bot)
    if id not in chat_member:
        return
    string = query.query.strip()
    search = await query_msg(string)
    for file in search:
        try:
            results.append(
                InlineQueryResultPhoto(
                    photo_url=await get_thumbnail(file),
                    thumb_url=await get_thumbnail(file),
                    photo_width=300,
                    photo_height=300,
                    input_message_content=InputTextMessageContent(
                        Presets.RESULTS.format(file.name,
                                               file.dept.upper(),
                                               file.mobile,
                                               file.extension,
                                               file.mail,
                                               file.emp,
                                               )
                    ),
                    description=Presets.DESCRIPTION_TXT.format(file.name, file.dept.upper(), file.mobile),
                    reply_markup=get_reply_markup(user_name[id])
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
    #
    user = await bot.get_users(id)
    global queried_user
    queried_user[id] = user.mention()
    await asyncio.sleep(5)
    results.clear()
