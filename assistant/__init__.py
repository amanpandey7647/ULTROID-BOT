# Ultroid - UserBot
# Copyright (C) 2020 ULTROID-OP
#
# This file is a part of < https://github.com/ULTROID-OP/ULTROID-BOT/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/ULTROID-OP/Ultroid/blob/main/LICENSE/>.

from pyUltroid import *
from pyUltroid.dB.database import Var
from telethon import Button, custom

OWNER_NAME = ultroid_bot.me.first_name
OWNER_ID = ultroid_bot.me.id


async def setit(event, name, value):
    try:
        udB.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")
