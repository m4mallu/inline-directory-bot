#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : inline-directory-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/inine-directory-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3

import os
from pyrogram import Client
from pyrogram.enums import ParseMode


if bool(os.environ.get("ENV", False)):
    from sample_config import Config
    from sample_config import LOGGER
else:
    from config import Config
    from config import LOGGER


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="bot",
            bot_token=Config.TG_BOT_TOKEN,
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            sleep_threshold=60,
            plugins={
                "root": "plugins"
            },
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{me.username}  started! "
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")


app = Bot()
app.run()

