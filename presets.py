#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : inline-directory-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/inine-directory-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3


class Presets(object):
    RESULTS = """
<b>Name  - {}
Dept    - {}
Mobile-</b> {}
<b>Ext.</b>      - {}
<b>Email  - <code>{}</code>
EMP    - {}</b>\xad                                                                     \xad
    """
    SUPPORT_TXT = """
<b>For :</b>
<code>- Queries
- Suggestions
- Reporting Bugs</code>

🔰<b> Please contact the Developer</b> 🔰
    """
    NOT_AUTH_TEXT_CB = """
❌ You are not authorized ❌
----------------------------------------------
You are not a member in the official channel / group configured in this bot
"""
    NOT_AUTH_TEXT_GEN_CB = """
❌ You are not authorized ❌
----------------------------------------------
The function you are trying to perform is only available to the sudo users of this bot. 
"""
    RESET_TXT = """
Success:  ✅
--------------------
The system has been rebooted !
"""
    WELCOME_TXT = "<b>Hello.. {} 🙋🏻</b>\n<i>Tap '<strike>Search Here</strike>' to search inline. " \
                  "Try '<strike>Help</strike>' to know, how to use this bot." \
                  " If you have any difficulty to use this bot, please contact the support. To make a copy of mine, " \
                  " please visit my <u>Github Source Repo</u>. Have a nice day 👏</i>"
    HELP_TXT = "<b>Select the appropriate button to know the functions and usages of this bot.</b>"
    THUMBNAIL_URL = 'https://telegra.ph/file/06610b5b61f20d1dcb38a.png'
    NO_RESULT_TXT = "❌ No results:"
    NO_RESULT_TXT_STR = "😥 No results for 👉 {}"
    RESULT_TXT = "👀 Results:"
    DL_WAIT_MSG = "<b>Downloading... Please wait</b>"
    WAIT_MSG = "<b>Processing...⏳</b>"
    WAIT_MSG_LONG = "<u><b>Processing... Plz wait</b></u> ⏱\n<i>This may take some time...</i>"
    MASS_DEL_CNF = "<b> Deleted the record, if exist</b> ✅"
    NO_USER_MSG = "<b>Error:</b>\n\n<i>User not found in database</i>"
    CSV_LOAD_CNF = "<b>Success:</b> ✅\n\n<i>Datas in <code>{}</code>\nhad been successfully loaded to the bot database</i>"
    CSV_ERROR = "<b>Error:</b>\n\n<i>Check the 👉 <code>{}</code>\nand try again later.. !</i>"
    URL_ERROR = "<b>Error:</b>\n\n<i>Something went wring ! Try again later with a different file..!</i>"
    NOT_AUTH_TEXT = "<b>Error:</b>\n\n<i>You are not authorized to perform this function. Contact support !</i>"
    USER_ADDED_MSG = "<b>Success:</b> ✅\n\n<i>User has been added to the database.</i>"
    USER_UPDATED_MSG = "<b>Success:</b> ✅\n\n<i>User exists, updated to the database</i>"
    SHARE_BUTTON_TEXT = "Hi..  👋\nUse @{} for searching contacts amoung our institution."
    UPDATE_EXT_CNF = "<b>Success:</b> ✅\n\n<i>Extension number of <b>{}</b> has been updated to : <code>{}</code></i>"
    UPDATE_EXT_ERROR = "<b>Error:</b>\n\n<i>Employee code not found in my database </i> 😢"
    IMG_UPLOAD_CNF = "<b>Success:</b> ✅\n\n<i>Image updated in database for emp:</i> <b>{}</b>\n\n" \
                     "<b>Open <a href='{}'>Here</a></b>\n\n<b>Copy Here</b> <code>{}</code>"
    UPDATE_MOBILE_TXT = "<b>Success:</b> ✅\n\n<i>Mobile number updated successfully</i>"
    UPDATE_EMAIL = "<b>Success:</b> ✅\n\n<i>Email id updated successfully</i>"
    INVALID_OPERATION = "<b><u>Invalid Operation</u></b> ⚠️\n\n1️⃣ <code>Click the button</code> <b>HELP</b>\n" \
                        "2️⃣ <code>Know the functions and usage.</code>\n3️⃣ <code>Try again later... </code>"
    ADMINS_INFO = "<b>Admins of this bot [{}]</b>\n"
    BROADCAST_MSG = "<b>Message send successfully: ✅\n\xad                                   \xad\nPassed- {}\nFailed- {}</b>"
    DESCRIPTION_TXT = "{} | {} | {} |"
    BOT_USERS = "<b>Total users of this bot [{}]</b>\n{}"
    SEARCH_RESULT_LOG = "🔍 <b>SEARCHED</b> 🔎\n\nPerson: {}\n\nResult: <b>{}</b>"
