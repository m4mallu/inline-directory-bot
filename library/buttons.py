#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : inline-directory-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/inine-directory-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


help_button = [
    [
        InlineKeyboardButton("Help", callback_data="help_btn"),
        InlineKeyboardButton("Source", url="https://github.com/m4mallu/inline-directory-bot")
    ],
    [
        InlineKeyboardButton("Support", callback_data="support_btn"),
        InlineKeyboardButton("Search Here", switch_inline_query_current_chat='')
    ]
]


back_button = [
    [
        InlineKeyboardButton("⬅️ Back", callback_data="back_btn")
    ]
]

reply_markup_back = InlineKeyboardMarkup(back_button)
reply_markup_help = InlineKeyboardMarkup(help_button)
