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
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from library.buttons import reply_markup_help
from library.support import get_reply_markup, admin_info
from library.sql import (query_emp,
                         add_user,
                         update_user,
                         update_thumb,
                         load_db,
                         mass_delete,
                         update_extension,
                         update_mobile_num,
                         update_email)


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
        msg = await m.reply_text(Presets.NOT_AUTH_TEXT)
        await m.delete()
        await asyncio.sleep(5)
        await msg.delete()
        return
    #
    count_emp = len(m.text.split(" ")[1:])
    if (count_emp in range(6, 7)) == bool(0):
        msg = await m.reply_text(Presets.INVALID_FORMAT)
        await m.delete()
        await asyncio.sleep(10)
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
    if bool(query) == bool(0):
        await add_user(name, dept, mobile, extension, mail, emp, 0)
        msg = await m.reply_text(Presets.USER_ADDED_MSG)
        await asyncio.sleep(5)
        await msg.delete()
    else:
        await update_user(name, dept, mobile, extension, mail, emp)
        msg = await m.reply_text(Presets.USER_UPDATED_MSG)
        await asyncio.sleep(5)
        await msg.delete()


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
    me = await Client.get_me(b)
    msg = await m.reply_text(Presets.DL_WAIT_MSG)
    if m.from_user.id not in Config.ADMIN_USERS:
        await msg.edit_text(Presets.NOT_AUTH_TEXT)
        await m.delete()
        await asyncio.sleep(5)
        await msg.delete()
        return
    #
    if (" " in m.text) and (m.reply_to_message is not None) and m.reply_to_message.photo:
        try:
            emp = str(m.text).split(" ")[1]
        except Exception:
            msg = await m.reply_text(Presets.INVALID_CMD)
            await m.delete()
            await asyncio.sleep(5)
            await msg.delete()
            return
        status = await query_emp(emp)
        if bool(status) == bool(0):
            await msg.edit_text(Presets.NO_USER_MSG)
            await m.delete()
            await asyncio.sleep(5)
            await msg.delete()
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
                            parse_mode='html',
                            disable_web_page_preview=True,
                            reply_markup=get_reply_markup(me.username)
                            )
        try:
            # Removing downloaded image from bot local
            os.remove(thumb_path)
        except Exception:
            pass
    else:
        await m.delete()
        await msg.edit_text(Presets.INVALID_IMG)
        await asyncio.sleep(5)
        await msg.delete()


# ----------------- add csv data to db table [Admin] ---------------------- #
# --- Steps:
# 1.Checking the csv file extension
# 2.Checking the row length in csv file
# 3.Iterating csv data
# 4.Add data to db table
@Client.on_message(filters.private & filters.command('load'))
async def load_database(b, m: Message):
    if m.from_user.id not in Config.ADMIN_USERS:
        msg = await m.reply_text(Presets.NOT_AUTH_TEXT)
        await m.delete()
        await asyncio.sleep(5)
        await msg.delete()
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
                await msg.edit_text(Presets.CSV_ERROR.format(file.document.file_name))
                await asyncio.sleep(5)
                await msg.delete()
                os.remove(file_name)
                return
            else:
                try:
                    await load_db(file_name)
                    await msg.edit_text(Presets.CSV_LOAD_CNF.format(file.document.file_name))
                    await asyncio.sleep(5)
                    await msg.delete()
                except Exception:
                    await msg.edit_text(Presets.CSV_ERROR.format(file.document.file_name))
                    await asyncio.sleep(5)
                    await msg.delete()
            os.remove(file_name)
    else:
        msg = await m.reply_text(Presets.NO_CSV_MSG)
        await m.delete()
        await asyncio.sleep(5)
        await msg.delete()


# ------------------------- mass delete records [Admin] -------------------- #
@Client.on_message(filters.private & filters.command('delete'))
async def mass_delete_emp(b, m: Message):
    msg = await m.reply_text(Presets.WAIT_MSG)
    if m.from_user.id not in Config.ADMIN_USERS:
        await msg.edit_text(Presets.NOT_AUTH_TEXT)
        await m.delete()
        await asyncio.sleep(5)
        await msg.delete()
        return
    if " " in m.text:
        emp_list = m.text.split(" ")[1:]
        await mass_delete(emp_list)
        await m.delete()
        await msg.edit_text(Presets.MASS_DEL_CNF)
        await asyncio.sleep(5)
        await msg.delete()
    else:
        await m.delete()
        await msg.edit_text(Presets.MASS_DEL_ERROR)
        await asyncio.sleep(5)
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
        await asyncio.sleep(e.x)
    except Exception:
        msg = await m.reply_text(Presets.NOT_AUTH_TEXT)
        await m.delete()
        await asyncio.sleep(5)
        await msg.delete()
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
            await msg.edit_text(Presets.UPDATE_EXT_ERROR)
            await asyncio.sleep(5)
            await msg.delete()
            return
        await m.delete()
        await msg.edit_text(Presets.UPDATE_EXT_CNF.format(emp, ext))
        await asyncio.sleep(5)
        await msg.delete()
    else:
        await m.delete()
        await msg.edit_text(Presets.UPDATE_EXT_FORMAT_ERROR)
        await asyncio.sleep(5)
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
        await asyncio.sleep(e.x)
    except Exception:
        msg = await m.reply_text(Presets.NOT_AUTH_TEXT)
        await m.delete()
        await asyncio.sleep(5)
        await msg.delete()
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
            await msg.edit_text(Presets.NO_USER_MSG)
            await m.delete()
            await asyncio.sleep(5)
            await msg.delete()
            return
        if bool(m1 and m2):
            mobile_numbers = str(m1) + " " + "|" + " " + str(m2)
        else:
            mobile_numbers = str(m1)
        await update_mobile_num(emp, mobile_numbers)
        await m.delete()
        await msg.edit_text(Presets.UPDATE_MOBILE_TXT)
        await asyncio.sleep(5)
        await msg.delete()
    else:
        await m.delete()
        await msg.edit_text(Presets.LIMIT_MOBILE)
        await asyncio.sleep(5)
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
        await asyncio.sleep(e.x)
    except Exception:
        msg = await m.reply_text(Presets.NOT_AUTH_TEXT)
        await m.delete()
        await asyncio.sleep(5)
        await msg.delete()
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
            await msg.edit_text(Presets.NO_USER_MSG)
            await m.delete()
            await asyncio.sleep(5)
            await msg.delete()
            return
        await update_email(emp, email)
        await m.delete()
        await msg.edit_text(Presets.UPDATE_EMAIL)
        await asyncio.sleep(5)
        await msg.delete()
    else:
        await m.delete()
        await msg.edit_text(Presets.UPDATE_EMAIL_ERROR)
        await asyncio.sleep(5)
        await msg.delete()

@Client.on_message(filters.private & filters.command('admins'))
async def view_admins(bot, m: Message):
    id = m.from_user.id
    try:
        member_status = await bot.get_chat_member(chat_id=Config.DEFAULT_CHAT_ROOM,
                                                  user_id=id
                                                  )
    except FloodWait as e:
        await asyncio.sleep(e.x)
    except Exception:
        msg = await m.reply_text(Presets.NOT_AUTH_TEXT)
        await m.delete()
        await asyncio.sleep(5)
        await msg.delete()
        return
    results = await admin_info(bot)
    message = '\n'.join(results)
    await m.delete()
    msg = await m.reply_text(Presets.ADMINS_INFO.format(message),
                             parse_mode='html',
                             disable_web_page_preview=True
                             )
    await asyncio.sleep(30)
    await msg.delete()
