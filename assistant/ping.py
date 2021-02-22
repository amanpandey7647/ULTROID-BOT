# Ultroid - UserBot
# Copyright (C) 2020 ULTROID-OP
#
# This file is a part of < https://github.com/ULTROID-OP/ULTROID-BOT/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/ULTROID-OP/Ultroid/blob/main/LICENSE/>.

from datetime import datetime


@asst_cmd("ping")
@owner
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await asst.send_message(
        event.chat_id,
        f"**Pong!!**\n `{ms}ms`",
    )
