#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : inline-directory-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/inine-directory-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3


from presets import Presets
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from library.buttons import reply_markup_back, reply_markup_help


@Client.on_callback_query(filters.regex(r'^support_btn$'))
async def bot_support(c, cb: CallbackQuery):
    me = await Client.get_me(c)
    await cb.answer()
    await cb.message.edit_text(Presets.SUPPORT_TXT,
                               parse_mode='html',
                               disable_web_page_preview=True,
                               reply_markup=reply_markup_back
                               )


@Client.on_callback_query(filters.regex(r'^back_btn$'))
async def back_to_start(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit_text(Presets.WELCOME_TXT.format(cb.from_user.first_name),
                               reply_markup=reply_markup_help
                               )


@Client.on_callback_query(filters.regex(r'^help_btn$'))
async def help_text(c, cb: CallbackQuery):
    await cb.answer()
    await cb.edit_message_text(Presets.HELP_TXT,
                               reply_markup=reply_markup_back,
                               parse_mode='html',
                               disable_web_page_preview=True
                               )

@Client.on_callback_query(filters.regex(r'^close_btn$'))
async def close_button(c, cb: CallbackQuery):
    await cb.message.delete()
