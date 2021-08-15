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
EMP    - {}</b>
\xad                                                                               \xad
<a href='t.me/{}?start={}'>🏠 <b>𝖧𝗈𝗆𝖾</b></a>
    """
    SUPPORT_TXT = """
𝙁𝙤𝙧 :
- 𝐐𝐮𝐞𝐫𝐢𝐞𝐬
- 𝐒𝐮𝐠𝐠𝐞𝐬𝐬𝐢𝐨𝐧𝐬
- 𝐑𝐞𝐩𝐨𝐫𝐭𝐢𝐧𝐠 𝐁𝐮𝐠𝐬


░▒▓ <a href='https://telegra.ph/inline-directory-bot-help-06-19'>𝐃𝐨𝐜𝐮𝐦𝐞𝐧𝐭𝐚𝐭𝐢𝐨𝐧</a> ▓▒░ <a href='https://t.me/space4renjith'>𝙍𝙚𝙣𝙟𝙞𝙩𝙝 𝙍</a>

    """
    NOT_AUTH_TEXT_CB = """
❌ 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗻𝗼𝘁 𝗮𝘂𝘁𝗵𝗼𝗿𝗶𝘇𝗲𝗱 ❌
----------------------------------------------
𝘠𝘰𝘶 𝘢𝘳𝘦 𝘯𝘰𝘵 𝘢 𝘮𝘦𝘮𝘣𝘦𝘳 𝘪𝘯 𝘵𝘩𝘦 𝘰𝘧𝘧𝘪𝘤𝘪𝘢𝘭 𝘤𝘩𝘢𝘯𝘯𝘦𝘭 / 𝘨𝘳𝘰𝘶𝘱 𝘤𝘰𝘯𝘧𝘪𝘨𝘶𝘳𝘦𝘥 𝘪𝘯 𝘵𝘩𝘪𝘴 𝘣𝘰𝘵 !
"""
    WELCOME_TXT = "<b>Hello.. {} 🙋🏻</b>\n<i>Tap '<strike>Search Here</strike>' to search inline. " \
                  "Try '<strike>Help</strike>' to know, how to use this bot." \
                  " If you have any difficulty to use this bot, please contact the support. To make a copy of mine, " \
                  " please visit my <u>Github Source Repo</u>. Have a nice day 👏</i>"
    HELP_TXT = "<b>Select the appropriate button to know the functions and usages of this bot.</b>"
    THUMBNAIL_URL = 'https://telegra.ph/file/06610b5b61f20d1dcb38a.png'
    NO_RESULT_TXT = "❌ 𝐍𝐨 𝐫𝐞𝐬𝐮𝐥𝐭𝐬:"
    NO_RESULT_TXT_STR = "😥 𝐍𝐨 𝐫𝐞𝐬𝐮𝐥𝐭𝐬 𝐟𝐨𝐫 👉 {}"
    RESULT_TXT = "👀 𝐑𝐞𝐬𝐮𝐥𝐭𝐬:"
    DL_WAIT_MSG = "𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙞𝙣𝙜 .. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩"
    WAIT_MSG = "𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴... 𝗣𝗹𝘇 𝘄𝗮𝗶𝘁 ⏱"
    WAIT_MSG_LONG = "<u>𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴... 𝗣𝗹𝘇 𝘄𝗮𝗶𝘁</u> ⏱\n<i>This may take some time...</i>"
    MASS_DEL_CNF = "𝘿𝙚𝙡𝙚𝙩𝙚𝙙 𝙩𝙝𝙚 𝙜𝙞𝙫𝙚𝙣 𝙧𝙚𝙘𝙤𝙧𝙙, 𝙞𝙛 𝙚𝙭𝙞𝙨𝙩 ! ✅"
    MASS_DEL_ERROR = "𝙀𝙧𝙧𝙤𝙧: <b>Invalid format</b>\n\n<i>Format: /delete emp1 emp2 ... emp'n'</i>"
    NO_USER_MSG = "𝙀𝙧𝙧𝙤𝙧:\n\n𝙐𝙨𝙚𝙧 𝙣𝙤𝙩 𝙛𝙤𝙪𝙣𝙙 𝙞𝙣 𝙙𝙖𝙩𝙗𝙖𝙨𝙚 !"
    CSV_LOAD_CNF = "𝐕𝐚𝐥𝐮𝐞𝐬 𝐢𝐧 <code>{}</code>\n𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐥𝐨𝐚𝐝𝐞𝐝 𝐭𝐨 𝐃𝐁 ✅"
    CSV_ERROR = "𝙀𝙧𝙧𝙤𝙧:\n\n𝐂𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 👉 <code>{}</code>\n𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧 𝐥𝐚𝐭𝐞𝐫..!"
    URL_ERROR = "𝙀𝙧𝙧𝙤𝙧:\n\n𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐰𝐞𝐧𝐭 𝐰𝐫𝐨𝐧𝐠\n𝐓𝐫𝐲 𝐰𝐢𝐭𝐡 𝐝𝐢𝐟𝐟𝐞𝐫𝐞𝐧𝐭 𝐟𝐢𝐥𝐞 !"
    NOT_AUTH_TEXT = "𝙀𝙧𝙧𝙤𝙧:\n\n𝐘𝐨𝐮 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐚𝐮𝐭𝐡𝐨𝐫𝐢𝐳𝐞𝐝 𝐩𝐞𝐫𝐟𝐨𝐫𝐦\n𝐭𝐡𝐢𝐬 𝐟𝐮𝐧𝐜𝐭𝐢𝐨𝐧.𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐬𝐮𝐩𝐩𝐨𝐫𝐭 ⚠️"
    USER_ADDED_MSG = "𝙐𝙨𝙚𝙧 𝙖𝙙𝙙𝙚𝙙 𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 ✅"
    USER_UPDATED_MSG = "𝙐𝙨𝙚𝙧 𝙚𝙭𝙞𝙨𝙩𝙨: 𝐔𝐩𝐝𝐚𝐭𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅"
    NO_CSV_MSG = "𝐒𝐞𝐧𝐝 𝐭𝐡𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝 𝐚𝐬 𝐚 𝐫𝐞𝐩𝐥𝐚𝐲 𝐭𝐨 𝐚\n𝐜𝐨𝐦𝐩𝐚𝐭𝐢𝐚𝐛𝐥𝐞 𝘾𝙎𝙑 𝐟𝐢𝐥𝐞"
    SHARE_BUTTON_TEXT = "𝙃𝙞..  👋\n𝐂𝐡𝐞𝐜𝐤𝐨𝐮𝐭 : @{}\n𝐅𝐨𝐫 𝐬𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 𝐜𝐨𝐧𝐭𝐚𝐜𝐭𝐬"
    INVALID_FORMAT = "𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙛𝙤𝙧𝙢𝙖𝙩:\n\n𝐅𝐨𝐫𝐦𝐚𝐭 𝐬𝐡𝐨𝐮𝐥𝐝 𝐛𝐞:\n<code>name dept mobile Ext.No mail emp [𝑤𝑖𝑡ℎ 𝑠𝑝𝑎𝑐𝑒 𝑠𝑒𝑝𝑎𝑟𝑎𝑡𝑖𝑜𝑛]</code>"
    INVALID_CMD = "𝙀𝙧𝙧𝙤𝙧:\n\n𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐟𝐨𝐫𝐦𝐚𝐭 ⚠️\n<code>Sample: /add 255</code>"
    UPDATE_EXT_CNF = "𝐄𝐱𝐭𝐞𝐧𝐬𝐢𝐨𝐧 𝐧𝐮𝐦𝐛𝐞𝐫 𝐟𝐨𝐫 𝐞𝐦𝐩𝐥𝐨𝐲: <code>{}</code>\n𝐇𝐚𝐬 𝐛𝐞𝐞𝐧 𝐮𝐩𝐝𝐚𝐭𝐞𝐝 𝐭𝐨: <code>{}</code>  ✅\n\n" \
                     "𝐂𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐮𝐩𝐝𝐚𝐭𝐞 𝐚𝐟𝐭𝐞𝐫 𝐬𝐨𝐦𝐞 𝐭𝐢𝐦𝐞 !"
    UPDATE_EXT_ERROR = "𝙀𝙧𝙧𝙤𝙧:\n\n𝐄𝐦𝐩𝐥𝐨𝐲𝐞𝐞 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝 𝐢𝐧 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞"
    UPDATE_EXT_FORMAT_ERROR = "𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙛𝙤𝙧𝙢𝙖𝙩:\n\n𝐅𝐨𝐫𝐦𝐚𝐭 𝐬𝐡𝐨𝐮𝐥𝐝 𝐛𝐞:\n<i>/extension emp ext.No</i>"
    INVALID_IMG = "𝙀𝙧𝙧𝙤𝙧: <b>Invalid Procedure</b>\n\n<i>Send a photo to this bot chat. As a reply to the photo use the " \
                  "command- /photo emp</i>"
    IMG_UPLOAD_CNF = "𝘾𝙤𝙣𝙜𝙧𝙖𝙩𝙨 :\n\n𝘐𝘮𝘢𝘨𝘦 𝘶𝘱𝘥𝘢𝘵𝘦𝘥 𝘴𝘶𝘤𝘤𝘦𝘴𝘴𝘧𝘶𝘭𝘭𝘺 𝘪𝘯 𝘥𝘢𝘵𝘢𝘣𝘢𝘴𝘦 𝘧𝘰𝘳 𝘦𝘮𝘱: <b>{}</b>\n\n" \
                     "𝐎𝐩𝐞𝐧 <a href='{}'>𝐡𝐞𝐫𝐞</a>:\n\n𝐂𝐨𝐩𝐲 𝐡𝐞𝐫𝐞: <code>{}</code>"
    UPDATE_MOBILE_TXT = "𝐌𝐨𝐛𝐢𝐥𝐞 𝐧𝐮𝐦𝐛𝐞𝐫 𝐮𝐩𝐝𝐚𝐭𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲  ✅"
    LIMIT_MOBILE = "𝙀𝙧𝙧𝙤𝙧: <b>Invalid Format</b>\n\n<i>Format: /mobile emp Mob-1 Mob-2\nUse '0' " \
                   "before the mobile numbers.</i>"
    UPDATE_EMAIL = "𝐄-𝐌𝐚𝐢𝐥 𝐈𝐝 𝐮𝐩𝐝𝐚𝐭𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅"
    ADMINS_INFO = "𝐀𝐝𝐦𝐢𝐧𝐬 𝐨𝐟 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭:\xad                             \xad\n\n{}"
    UPDATE_EMAIL_ERROR = "𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙛𝙤𝙧𝙢𝙖𝙩:\n\n<b>Format Should be</b>\n\n<code>/email emp sample@gmail.com</code>"
    BROADCAST_MSG = "𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐬𝐞𝐧𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅\n\xad                                   \xad\n<b>Passed- {}\nFailed- {}</b>"
    BROADCAST_ERROR = "𝙀𝙧𝙧𝙤𝙧:\n\n<i>This command should be used as a reply to any messaged or media. Just format a text" \
                      " message or send a media to bot. Finally, send this command as reply to the above message to" \
                      " broadcast it to the bot subscribers.</i>"
    DESCRIPTION_TXT = "| {} | {} |"
    BOT_USERS = "<b>Total users : {}</b>\xad                             \xad\n<i>{}</i>"
    QUERY_USERS_ERROR = "𝙀𝙧𝙧𝙤𝙧:\n\n<i>Use only /users command to view the bot users</i>"
