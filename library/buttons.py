#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : inline-directory-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/inine-directory-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


help_button = [
    [
        InlineKeyboardButton("❓ Help", callback_data="help_btn"),
        InlineKeyboardButton("♨️ Source", url="https://github.com/m4mallu/inline-directory-bot")
    ],
    [
        InlineKeyboardButton("👷🏿‍♂️ Support", callback_data="support_btn"),
        InlineKeyboardButton("🔎  Search Here", switch_inline_query_current_chat='')
    ],
    [
        InlineKeyboardButton("❌  Close", callback_data="close_btn")
    ]
]


main_back = [
    [
        InlineKeyboardButton("⬅️ Back", callback_data="back_btn")
    ]
]

help_back = [
    [
        InlineKeyboardButton("⬅️ Back", callback_data="help_back_btn")
    ]
]

close_button = [
    [
        InlineKeyboardButton("Close", callback_data="close_btn")
    ]
]

help_objects = [
    [
        InlineKeyboardButton("📒 Add Contact", callback_data="add_btn"),
        InlineKeyboardButton("⛔️ Del Contact", callback_data="del_btn")
    ],
    [
        InlineKeyboardButton("📧  Add E-mail", callback_data="email_btn"),
        InlineKeyboardButton("📱 Add Mobile", callback_data="mobile_btn")
    ],
    [
        InlineKeyboardButton("📷  Add Photo", callback_data="photo_btn"),
        InlineKeyboardButton("☎️ Add Extension", callback_data="extension_btn")
    ],
    [
        InlineKeyboardButton("🔎  Find Admins", callback_data="admins_btn"),
        InlineKeyboardButton("⏳ Import Data", callback_data="import_btn")
    ],
    [
        InlineKeyboardButton("📡  Broadcast", callback_data="send_btn"),
        InlineKeyboardButton("📋 List Users", callback_data="users_btn")
    ],
    [
        InlineKeyboardButton("🔰 CMD Help", url='https://telegra.ph/How-to-update-contact-details-07-01'),
        InlineKeyboardButton("📚 Web Docs", url='https://telegra.ph/inline-directory-bot-help-06-19')
    ],
    [
        InlineKeyboardButton("⁉️ How to do", callback_data="how_to_btn"),
        InlineKeyboardButton("⬅️ BACK", callback_data="back_btn")
    ]
]

replay_markup_close = InlineKeyboardMarkup(close_button)
reply_markup_back = InlineKeyboardMarkup(main_back)
reply_markup_help = InlineKeyboardMarkup(help_button)
reply_markup_help_back = InlineKeyboardMarkup(help_back)
reply_markup_objects = InlineKeyboardMarkup(help_objects)
