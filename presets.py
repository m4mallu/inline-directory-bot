#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : inline-directory-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/inine-directory-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3


class Presets(object):
    RESULTS = """
𝐍𝐚𝐦𝐞  - <b>{}</b>
𝐃𝐞𝐩𝐭    - {}
𝐌𝐨𝐛𝐢𝐥𝐞- {}
𝐄𝐱𝐭.     - {}
𝐄𝐦𝐚𝐢𝐥  - <code>{}</code>
𝐄𝐌𝐏   - {}
\xad                                                                               \xad
<a href='t.me/{}?start={}'>🏠 <b>𝖧𝗈𝗆𝖾</b></a>
    """
    HELP_TXT = """
░▒▓ <b>Procedure:</b>
          <code>1. Tap the button 'Search Here'
    2. Search by the:
            - Name.
            - Phone Number.
            - Department.
    3. Tap the required result.</code>

░▒▓ <b>Advantages:</b>
          <code>1. Search inline in any chat.
    2. Admins user support.
    3. Mass delete / upload.
    4. User can update data.</code>
    
░▒▓ <a href='https://telegra.ph/How-to-update-contact-details-07-01'>𝙐𝙥𝙙𝙖𝙩𝙞𝙣𝙜 𝙩𝙝𝙚 𝙘𝙤𝙣𝙩𝙖𝙘𝙩 𝙙𝙚𝙩𝙖𝙞𝙡𝙨</a>
 
░▒▓ <a href='https://telegra.ph/inline-directory-bot-help-06-19'>𝙋𝙧𝙤𝙟𝙚𝙘𝙩 𝙙𝙤𝙘𝙪𝙢𝙚𝙣𝙩𝙖𝙞𝙤𝙣</a>
    
░▒▓ <i>For any queries, contact SUPPORT</i>
    """
    SUPPORT_TXT = """
𝙁𝙤𝙧 :
- 𝐐𝐮𝐞𝐫𝐢𝐞𝐬
- 𝐒𝐮𝐠𝐠𝐞𝐬𝐬𝐢𝐨𝐧𝐬
- 𝐑𝐞𝐩𝐨𝐫𝐭𝐢𝐧𝐠 𝐁𝐮𝐠𝐬


░▒▓ <a href='https://telegra.ph/inline-directory-bot-help-06-19'>𝐃𝐨𝐜𝐮𝐦𝐞𝐧𝐭𝐚𝐭𝐢𝐨𝐧</a> ▓▒░ <a href='https://t.me/space4renjith'>𝙍𝙚𝙣𝙟𝙞𝙩𝙝 𝙍</a>

    """
    WELCOME_TXT = "<b>Hello.. {} 🙋🏻</b>\n<i>Tap '<strike>Search Here</strike>' to search inline. " \
                  "Try '<strike>Help</strike>' to know, how to use this bot." \
                  " If you have any difficulty to use this bot, please contact the support. To make a copy of mine, " \
                  " please visit my <u>Github Source Repo</u>. Have a nice day 👏</i>"
    THUMBNAIL_URL = 'https://telegra.ph/file/06610b5b61f20d1dcb38a.png'
    NO_RESULT_TXT = "❌ 𝐍𝐨 𝐫𝐞𝐬𝐮𝐥𝐭𝐬:"
    NO_RESULT_TXT_STR = "😥 𝐍𝐨 𝐫𝐞𝐬𝐮𝐥𝐭𝐬 𝐟𝐨𝐫 👉 {}"
    RESULT_TXT = "👀 𝐑𝐞𝐬𝐮𝐥𝐭𝐬:"
    DL_WAIT_MSG = "𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙞𝙣𝙜 .. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩"
    WAIT_MSG = "𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴... 𝗣𝗹𝘇 𝘄𝗮𝗶𝘁 ⏱"
    MASS_DEL_CNF = "𝘿𝙚𝙡𝙚𝙩𝙚𝙙 𝙩𝙝𝙚 𝙜𝙞𝙫𝙚𝙣 𝙧𝙚𝙘𝙤𝙧𝙙, 𝙞𝙛 𝙚𝙭𝙞𝙨𝙩 ! ✅"
    MASS_DEL_ERROR = "𝙋𝙡𝙚𝙖𝙨𝙚 𝙜𝙞𝙫𝙚 𝙩𝙝𝙚 𝙫𝙖𝙡𝙪𝙚𝙨 𝙨𝙚𝙥𝙖𝙧𝙖𝙩𝙚𝙙\n𝙗𝙮 𝙎𝙋𝘼𝘾𝙀 𝙛𝙤𝙡𝙡𝙤𝙬𝙚𝙙 𝙗𝙮 𝙩𝙝𝙚 𝙘𝙤𝙢𝙢𝙖𝙣𝙙 !"
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
    INVALID_IMG = "𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐬𝐡𝐨𝐮𝐥𝐝 𝐫𝐞𝐩𝐥𝐚𝐲 𝐭𝐨 𝐚𝐧𝐲 𝐩𝐡𝐨𝐭𝐨 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐢𝐧 𝐭𝐞𝐥𝐞𝐠𝐫𝐚𝐦"
    IMG_UPLOAD_CNF = "𝘾𝙤𝙣𝙜𝙧𝙖𝙩𝙨 :\n\n𝘐𝘮𝘢𝘨𝘦 𝘶𝘱𝘥𝘢𝘵𝘦𝘥 𝘴𝘶𝘤𝘤𝘦𝘴𝘴𝘧𝘶𝘭𝘭𝘺 𝘪𝘯 𝘥𝘢𝘵𝘢𝘣𝘢𝘴𝘦 𝘧𝘰𝘳 𝘦𝘮𝘱: <b>{}</b>\n\n" \
                     "𝐎𝐩𝐞𝐧 <a href='{}'>𝐡𝐞𝐫𝐞</a>:\n\n𝐂𝐨𝐩𝐲 𝐡𝐞𝐫𝐞: <code>{}</code>"
    UPDATE_MOBILE_TXT = "𝐌𝐨𝐛𝐢𝐥𝐞 𝐧𝐮𝐦𝐛𝐞𝐫 𝐮𝐩𝐝𝐚𝐭𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲  ✅"
    LIMIT_MOBILE = "𝐌𝐚𝐱𝐢𝐦𝐮𝐦 𝐓𝐰𝐨 𝐌𝐨𝐛𝐢𝐥𝐞 𝐧𝐮𝐦𝐛𝐞𝐫𝐬 𝐚𝐫𝐞\n𝐚𝐥𝐥𝐨𝐰𝐞𝐝, 𝐚𝐧𝐝 𝐬𝐡𝐨𝐮𝐥𝐝 𝐜𝐨𝐧𝐭𝐚𝐢𝐧 𝐢𝐧𝐭𝐞𝐠𝐞𝐫𝐬 "
    UPDATE_EMAIL = "𝐄-𝐌𝐚𝐢𝐥 𝐈𝐝 𝐮𝐩𝐝𝐚𝐭𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅"
    ADMINS_INFO = "𝐀𝐝𝐦𝐢𝐧𝐬 𝐨𝐟 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭:\xad                             \xad\n\n{}"
    UPDATE_EMAIL_ERROR = "𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙛𝙤𝙧𝙢𝙖𝙩:\n\n<b>Format Should be</b>\n\n<code>/email 251 sample@gmail.com</code>"
    BROADCAST_MSG = "𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐬𝐞𝐧𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅\n\xad                                   \xad\n<b>Passed- {}\nFailed- {}</b>"
    BROADCAST_ERROR = "𝙀𝙧𝙧𝙤𝙧:\n\n<i>This command should be used as a reply to any messaged or media. Just format a text" \
                      " message or send a media to bot. Finally, send this command as reply to the above message to" \
                      " broadcast it to the bot subscribers.</i>"
    DESCRIPTION_TXT = "| {} | {} |"
