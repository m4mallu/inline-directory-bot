#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : inline-directory-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/inine-directory-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3

import os
import csv
import codecs
import asyncio
from PIL import Image
from presets import Presets
from telegraph import upload_file
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from hachoir.parser import createParser
from plugins.inline import queried_user
from hachoir.metadata import extractMetadata
from pyrogram.enums import ParseMode, ChatAction
from pyrogram.types import Message, InlineKeyboardMarkup
from library.support import map_chat_member, gen_user_markups
from library.buttons import reply_markup_help, replay_markup_close, secial_close_btn, single_close_button
from library.sql import (query_emp,
                         add_user,
                         update_user,
                         update_thumb,
                         load_db,
                         mass_delete,
                         update_extension,
                         update_mobile_num,
                         update_email,
                         get_all_data)


if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config


# -------------------------------- Start bot ------------------------ #
@Client.on_message(filters.private & filters.text & filters.command(['start', 'help']))
async def start_bot(c: Client, m: Message):
    await m.reply_text(
        Presets.WELCOME_TXT.format(m.from_user.first_name),
        reply_markup=reply_markup_help
    )
    await m.delete()


# ---------------- add user details command [Admin] ------------------- #
@Client.on_message(filters.private & filters.command('add'))
async def user_update(b, m: Message):
    if m.from_user.id not in Config.ADMIN_USERS:
        msg = await m.reply_text(
            Presets.NOT_AUTH_TEXT,
            reply_markup=replay_markup_close
        )
        await m.delete()
        return
    #
    count_emp = len(m.text.split(" ")[1:])
    if (count_emp in range(6, 7)) == bool(0):
        await m.delete()
        msg = await m.reply_text(Presets.INVALID_OPERATION)
        await asyncio.sleep(15)
        await msg.delete()
        return
    #
    name = str(m.text).split(" ")[1].replace("-", " ")
    dept = str(m.text).split(" ")[2]
    mobile = str(m.text).split(" ")[3]
    extension = str(m.text).split(" ")[4]
    mail = str(m.text).split(" ")[5]
    emp = str(m.text).split(" ")[6]
    #
    query = await query_emp(emp)
    if not bool(query):
        await add_user(name, dept, mobile, extension, mail, emp, 0)
        msg = await m.reply_text(
            Presets.USER_ADDED_MSG,
            reply_markup=replay_markup_close
        )
    else:
        await update_user(name, dept, mobile, extension, mail, emp)
        msg = await m.reply_text(
            Presets.USER_UPDATED_MSG,
            reply_markup=replay_markup_close
        )


# ------------- adding image url to db from photo [Admin] ------------- #
# --- Steps:
# 1.Download photo to bot local.
# 2.Resize it as a thumbnail.
# 3.Upload to telegra.ph
# 4.Get url from telegra.ph
# 5.Add url to corresponding db table
# 6.Share url to bot user
# 7.Removing photo from bot local
@Client.on_message(filters.private & filters.command('photo'))
async def add_thumb(b, m: Message):
    msg = await m.reply_text(Presets.DL_WAIT_MSG)
    if m.from_user.id not in Config.ADMIN_USERS:
        await msg.edit_text(
            Presets.NOT_AUTH_TEXT,
            reply_markup=replay_markup_close
        )
        await m.delete()
        return
    #
    if (" " in m.text) and (m.reply_to_message is not None) and m.reply_to_message.photo:
        try:
            emp = str(m.text).split(" ")[1]
        except Exception:
            await m.delete()
            msg = await m.reply_text(Presets.INVALID_OPERATION)
            await asyncio.sleep(15)
            await msg.delete()
            return
        status = await query_emp(emp)
        if not bool(status):
            await msg.edit_text(
                Presets.NO_USER_MSG,
                reply_markup=replay_markup_close
            )
            await m.delete()
            return
        reply_message = m.reply_to_message
        # Downloading photo to bot local
        thumb_path = await reply_message.download()
        # Getting downloaded image size
        width = height = 0
        metadata = extractMetadata(createParser(thumb_path))
        if metadata.has("width"):
            width = metadata.get("width")
        if metadata.has("height"):
            height = metadata.get("height")
        # resizing image
        Image.open(thumb_path).convert("RGB").save(thumb_path)
        img = Image.open(thumb_path)
        # img.thumbnail((90, 90))
        img.resize((320, height))
        img.save(thumb_path, "JPEG")
        # Uploading file to telegra.ph
        try:
            img_url = upload_file(thumb_path)[0]
        except Exception:
            try:
                os.remove(thumb_path)
            except Exception:
                pass
            await msg.edit_text(Presets.URL_ERROR)
            await asyncio.sleep(5)
            await msg.delete()
            return
        url = f"https://telegra.ph{img_url}"
        # Storing generated url to database
        await update_thumb(emp, url)
        await m.delete()
        # Sharing url to bot
        await msg.edit_text(Presets.IMG_UPLOAD_CNF.format(emp, url, url),
                            parse_mode=ParseMode.HTML,
                            disable_web_page_preview=True,
                            reply_markup=replay_markup_close)
        try:
            # Removing downloaded image from bot local
            os.remove(thumb_path)
        except Exception:
            pass
    else:
        await m.delete()
        await msg.edit(Presets.INVALID_OPERATION)
        await asyncio.sleep(15)
        await msg.delete()


# ----------------- add csv data to db table [Admin] ---------------------- #
# --- Steps:
# 1.Checking the csv file extension
# 2.Checking the row length in csv file
# 3.Iterating csv data
# 4.Add data to db table
@Client.on_message(filters.private & filters.command('load'))
async def load_database(b, m: Message):
    if m.from_user.id not in Config.SUDO_USERS:
        msg = await m.reply_text(
            Presets.NOT_AUTH_TEXT,
            reply_markup=replay_markup_close
        )
        await m.delete()
        return
    #
    file = m.reply_to_message
    if (file is not None) and (file.document.file_name.endswith('.csv')):
        msg = await m.reply_text(Presets.DL_WAIT_MSG)
        file_name = await file.download()
        await m.delete()
        # Opening the scv file to check the compatibility between db table and csv data #
        with codecs.open(file_name, "r", encoding='utf-8', errors='ignore') as f:
            reader = csv.reader(f, delimiter=",")
            data = list(reader)[1]
            row_count = len(data)
            # checking the first row length in given csv as 7 (db table length)#
            if (row_count in range(7, 8)) == bool(0):
                await msg.edit_text(
                    Presets.CSV_ERROR.format(file.document.file_name),
                    reply_markup=replay_markup_close
                )
                os.remove(file_name)
                return
            else:
                try:
                    await load_db(file_name)
                    await msg.edit_text(
                        Presets.CSV_LOAD_CNF.format(file.document.file_name),
                        reply_markup=replay_markup_close
                    )
                except Exception:
                    await msg.edit_text(
                        Presets.CSV_ERROR.format(file.document.file_name),
                        reply_markup=replay_markup_close
                    )
            os.remove(file_name)
    else:
        await m.delete()
        msg = await m.reply_text(Presets.INVALID_OPERATION)
        await asyncio.sleep(15)
        await msg.delete()


# ------------------------- mass delete records [Admin] -------------------- #
@Client.on_message(filters.private & filters.command('delete'))
async def mass_delete_emp(b, m: Message):
    msg = await m.reply_text(Presets.WAIT_MSG)
    if m.from_user.id not in Config.ADMIN_USERS:
        await msg.edit_text(
            Presets.NOT_AUTH_TEXT,
            reply_markup=replay_markup_close
        )
        await m.delete()
        return
    if " " in m.text:
        emp_list = m.text.split(" ")[1:]
        await mass_delete(emp_list)
        await m.delete()
        await msg.edit_text(
            Presets.MASS_DEL_CNF,
            reply_markup=replay_markup_close
        )
    else:
        await m.delete()
        await msg.edit(Presets.INVALID_OPERATION)
        await asyncio.sleep(15)
        await msg.delete()


# -------------------------------- Update Extension number -------------------------- #
@Client.on_message(filters.private & filters.command('extension'))
async def extension_update(bot, m: Message):
    id = m.from_user.id
    try:
        member_status = await bot.get_chat_member(chat_id=Config.DEFAULT_CHAT_ROOM,
                                                  user_id=id
                                                  )
    except FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception:
        msg = await m.reply_text(
            Presets.NOT_AUTH_TEXT,
            reply_markup=replay_markup_close
        )
        await m.delete()
        return
    cmd_count = len(m.text.split(" ")[1:])
    msg = await m.reply_text(Presets.WAIT_MSG)
    if (cmd_count in range(1, 3)) != bool(0) and str(m.text.split(" ")[1]).isdigit():
        emp = m.text.split(" ")[1]
        ext = m.text.split(" ")[2]
        try:
            await update_extension(emp, ext)
        except Exception:
            await m.delete()
            await msg.edit_text(
                Presets.UPDATE_EXT_ERROR,
                reply_markup=replay_markup_close
            )
            return
        await m.delete()
        await msg.edit_text(
            Presets.UPDATE_EXT_CNF.format(emp, ext),
            reply_markup=replay_markup_close
        )
    else:
        await m.delete()
        await msg.edit(Presets.INVALID_OPERATION)
        await asyncio.sleep(15)
        await msg.delete()


# --------------------------------- Update Mobile Number -------------------------------- #
@Client.on_message(filters.private & filters.command('mobile'))
async def update_mobile(bot, m: Message):
    id = m.from_user.id
    emp = m1 = m2 = int()
    mobile_numbers = str()
    try:
        member_status = await bot.get_chat_member(chat_id=Config.DEFAULT_CHAT_ROOM,
                                                  user_id=id
                                                  )
    except FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception:
        msg = await m.reply_text(
            Presets.NOT_AUTH_TEXT,
            reply_markup=replay_markup_close
        )
        await m.delete()
        return
    cmd_count = len(m.text.split(" ")[1:])
    msg = await m.reply_text(Presets.WAIT_MSG)
    if (cmd_count in range(1, 4)) != bool(0) and str(m.text.split(" ")[1]).isdigit():
        try:
            emp = m.text.split(" ")[1]
            m1 = m.text.split(" ")[2]
            m2 = m.text.split(" ")[3]
        except Exception:
            pass
        status = await query_emp(emp)
        if bool(status) == bool(0):
            await msg.edit_text(
                Presets.NO_USER_MSG,
                reply_markup=replay_markup_close
            )
            await m.delete()
            return
        if bool(m1 and m2):
            mobile_numbers = str(m1) + " " + "|" + " " + str(m2)
        else:
            mobile_numbers = str(m1)
        await update_mobile_num(emp, mobile_numbers)
        await m.delete()
        await msg.edit_text(
            Presets.UPDATE_MOBILE_TXT,
            reply_markup=replay_markup_close
        )
    else:
        await m.delete()
        await msg.edit(Presets.INVALID_OPERATION)
        await asyncio.sleep(15)
        await msg.delete()


# -------------------------------- Update E-Mail address -------------------------- #
@Client.on_message(filters.private & filters.command('email'))
async def update_email_id(bot, m: Message):
    id = m.from_user.id
    emp = email = str()
    try:
        member_status = await bot.get_chat_member(chat_id=Config.DEFAULT_CHAT_ROOM,
                                                  user_id=id
                                                  )
    except FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception:
        msg = await m.reply_text(
            Presets.NOT_AUTH_TEXT,
            reply_markup=replay_markup_close
        )
        await m.delete()
        return
    cmd_count = len(m.text.split(" ")[1:])
    msg = await m.reply_text(Presets.WAIT_MSG)
    if (cmd_count in range(1, 3)) and str(m.text.split(" ")[1]).isdigit():
        try:
            emp = m.text.split(" ")[1]
            email = m.text.split(" ")[2]
        except Exception:
            pass
        status = await query_emp(emp)
        if bool(status) == bool(0):
            await msg.edit_text(
                Presets.NO_USER_MSG,
                reply_markup=replay_markup_close
            )
            await m.delete()
            return
        await update_email(emp, email)
        await m.delete()
        await msg.edit_text(
            Presets.UPDATE_EMAIL,
            reply_markup=replay_markup_close
        )
    else:
        await m.delete()
        await msg.edit(Presets.INVALID_OPERATION)
        await asyncio.sleep(15)
        await msg.delete()


# -------------------------------- Get Admin List -------------------------- #
@Client.on_message(filters.private & filters.command('admins'))
async def view_admins(bot, m: Message):
    id = m.from_user.id
    msg = await m.reply_text(Presets.WAIT_MSG)
    try:
        member_status = await bot.get_chat_member(chat_id=Config.DEFAULT_CHAT_ROOM, user_id=id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception:
        await msg.edit(Presets.NOT_AUTH_TEXT, reply_markup=replay_markup_close)
        await m.delete()
        return
    await m.delete()
    #
    count = int()
    buttons = list()
    user = button = mention = str()
    #
    for admin in Config.ADMIN_USERS:
        try:
            user = await bot.get_users(admin)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception:
            pass
        else:
            count += 1
            mention = user.mention()
            button = await gen_user_markups(count, mention)
            buttons.append(button)
    buttons.append(secial_close_btn)
    await msg.delete()
    await m.reply_text(Presets.ADMINS_INFO.format(count), reply_markup=InlineKeyboardMarkup(buttons))


# --------------- function to broadcast the messages to the bot users ---------------- #
@Client.on_message(filters.private & filters.command('send'))
async def send_message_to_users(bot, m: Message):
    msg = await m.reply_text(Presets.WAIT_MSG)
    if m.from_user.id not in Config.SUDO_USERS:
        await msg.edit_text(
            Presets.NOT_AUTH_TEXT,
            reply_markup=replay_markup_close
        )
        await m.delete()
        return
    fail_count = pass_count = int()
    if (" " not in m.text) and ("send" in m.text) and (m.reply_to_message is not None):
        await m.delete()
        member = await map_chat_member(bot)
        for chat_id in member:
            try:
                await bot.send_chat_action(chat_id, ChatAction.TYPING)
            except Exception:
                fail_count += 1
                pass
            else:
                try:
                    await bot.copy_message(
                        chat_id=chat_id,
                        from_chat_id=m.chat.id,
                        message_id=m.reply_to_message_id,
                        caption=m.caption
                    )
                    pass_count += 1
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                except Exception:
                    pass
        await msg.delete()
        await m.reply_text(Presets.BROADCAST_MSG.format(pass_count, fail_count),
                           reply_markup=replay_markup_close
                           )
    else:
        await m.delete()
        await msg.edit(Presets.INVALID_OPERATION)
        await asyncio.sleep(15)
        await msg.delete()


# --------------------- Function to get the name-list of bot users ------------------- #
@Client.on_message(filters.private & filters.command('users'))
async def get_bot_users(bot, m: Message):
    msg = await m.reply_text(Presets.WAIT_MSG)
    if m.from_user.id not in Config.SUDO_USERS:
        await msg.edit_text(
            Presets.NOT_AUTH_TEXT,
            reply_markup=replay_markup_close
        )
        await m.delete()
        return
    if (" " not in m.text) and ("users" in m.text):
        await m.delete()
        count = int()
        user_list = []
        user = mention = result = str()
        user_ids = await map_chat_member(bot)
        for ids in user_ids:
            try:
                await bot.send_chat_action(ids, ChatAction.TYPING)
            except Exception:
                pass
            else:
                user = await bot.get_users(ids)
                mention = user.mention()
                user_list.append(mention)
        total_users = len(user_list)
        if total_users > 50:
            new_list = [user_list[i:i + 50] for i in range(0, len(user_list), 50)]
            for items in new_list:
                for item in items:
                    result = result + "\n" + "\n".join([item])
                await m.reply_text(
                    Presets.BOT_USERS.format(total_users, result),
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                    reply_markup=single_close_button
                )
                result = str()
            await msg.delete()
        else:
            for item in user_list:
                result = result + "\n" + "\n".join([item])
            await msg.edit_text(
                Presets.BOT_USERS.format(total_users, result),
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
                reply_markup=single_close_button
            )
    else:
        await m.delete()
        await msg.edit(Presets.INVALID_OPERATION)
        await asyncio.sleep(10)
        await msg.delete()


# --------------------- Function to get the currnet databse  as csv ------------------- #
@Client.on_message(filters.private & filters.command('download'))
async def save_database(bot, m: Message):
    id = m.from_user.id
    if Config.DEV_ID and id == Config.DEV_ID:
        await get_all_data()
        try:
            await m.reply_document(
                document=open('database.csv', 'rb'),
            )
        except Exception:
            await m.reply_text(
                text='Something went wrong!',
                reply_markup=replay_markup_close
            )
        try:
            os.remove('database.csv')
        except Exception:
            pass
        await m.delete()
    else:
        await m.reply_text(
            text=Presets.NOT_AUTH_TEXT,
            reply_markup=replay_markup_close
        )
        await m.delete()

# --------------------- Function to get the log updates for the dev id ------------------- #
@Client.on_message(filters.private & filters.incoming)
async def get_inline_result_selected_text(bot, m: Message):
    id = m.from_user.id
    if id in Config.SUDO_USERS:
        return
    elif (Config.DEV_ID is not None) and m.text.startswith('Name  -'):
        user_query = str(m.text).partition('\n')[0].replace('Name  - ', '')
        try:
            await bot.send_message(
                chat_id=Config.DEV_ID,
                text=Presets.SEARCH_RESULT_LOG.format(queried_user[id], user_query),
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
                reply_markup=replay_markup_close,
                disable_notification=True
            )
        except Exception:
            pass
    else:
        pass
