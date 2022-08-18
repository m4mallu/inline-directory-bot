#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : inline-directory-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/inine-directory-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3

import os
import sys
from help import Help
from presets import Presets
from pyrogram.enums import ParseMode
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from library.support import chat_member, query_chat_participant
from library.buttons import (reply_markup_back, reply_markup_help, reply_markup_objects,
                             reply_markup_help_back, reply_markup_support)


if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config


@Client.on_callback_query(filters.regex(r'^support_btn$'))
async def bot_support(c, cb: CallbackQuery):
    id = cb.from_user.id
    await query_chat_participant(id, c)
    if id not in chat_member:
        await cb.answer(Presets.NOT_AUTH_TEXT_CB, True)
        return
    await cb.answer()
    await cb.message.edit_text(Presets.SUPPORT_TXT,
                               parse_mode=ParseMode.HTML,
                               disable_web_page_preview=True,
                               reply_markup=reply_markup_support
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
                               reply_markup=reply_markup_objects,
                               parse_mode=ParseMode.HTML,
                               disable_web_page_preview=True
                               )

@Client.on_callback_query(filters.regex(r'^close_btn$'))
async def close_button(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.delete()


# ----------------------------------------------- Help Objects ---------------------------------------- #


@Client.on_callback_query(filters.regex(r'^help_back_btn$'))
async def help_back_button(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Presets.HELP_TXT,
                          reply_markup=reply_markup_objects,
                          disable_web_page_preview=True)


@Client.on_callback_query(filters.regex(r'^add_btn$'))
async def add_contact(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Help.ADD_CONTACT_TXT,
                          reply_markup=reply_markup_help_back)


@Client.on_callback_query(filters.regex(r'^del_btn$'))
async def delete_contact(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Help.DEL_CONTACT_TXT,
                          reply_markup=reply_markup_help_back)


@Client.on_callback_query(filters.regex(r'^email_btn$'))
async def update_email(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Help.ADD_EMAIL_TXT,
                          reply_markup=reply_markup_help_back)


@Client.on_callback_query(filters.regex(r'^mobile_btn$'))
async def update_mobile(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Help.ADD_MOBILE_TXT,
                          reply_markup=reply_markup_help_back)


@Client.on_callback_query(filters.regex(r'^photo_btn$'))
async def update_photo(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Help.ADD_PHOTO_TXT,
                          reply_markup=reply_markup_help_back)


@Client.on_callback_query(filters.regex(r'^extension_btn$'))
async def update_extension(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Help.ADD_EXTENSION_TXT,
                          reply_markup=reply_markup_help_back)


@Client.on_callback_query(filters.regex(r'^admins_btn$'))
async def find_admins(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Help.FIND_ADMINS_TXT,
                          reply_markup=reply_markup_help_back)


@Client.on_callback_query(filters.regex(r'^import_btn$'))
async def import_data(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Help.IMPORT_DATA_TXT,
                          reply_markup=reply_markup_help_back)


@Client.on_callback_query(filters.regex(r'^send_btn$'))
async def send_messages(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Help.BROADCAST_MSG_TXT,
                          reply_markup=reply_markup_help_back)


@Client.on_callback_query(filters.regex(r'^users_btn$'))
async def list_bot_users(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Help.LIST_USERS_TXT,
                          reply_markup=reply_markup_help_back)


@Client.on_callback_query(filters.regex(r'^how_to_btn$'))
async def bot_working(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Help.HOW_TO_DO_TXT,
                          reply_markup=reply_markup_help_back)


@Client.on_callback_query(filters.regex(r'^error_help_btn$'))
async def error_help_button(c, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(
        Presets.HELP_TXT,
        reply_markup=reply_markup_objects
    )


@Client.on_callback_query(filters.regex(r'^reboot_btn$'))
async def reboot_bot(c, cb: CallbackQuery):
    if cb.from_user.id not in Config.SUDO_USERS:
        await cb.answer(Presets.NOT_AUTH_TEXT_GEN_CB, True)
        return
    await cb.answer(Presets.RESET_TXT, True)
    os.execl(sys.executable, sys.executable, *sys.argv)
