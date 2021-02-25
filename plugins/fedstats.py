"""
✘ Commands Available -
• {i}fedstats <username> and .fstat <usrname or reply>
    Give fed releated info
"""

import asyncio
# ported from LEGENDBOT (LEGENDX) 
from telethon.errors.rpcerrorlist import YouBlockedUserError
from LEGEND import admin_cmd
borg = bot

bott = "@MissRose_bot"
LEGENDX = borg.me.first_name


@borg.on(admin_cmd("fstat ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit(f"CHECKING BY {LEGENDX}...")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        sysarg = str(previous_message.sender_id)
        user = f"[user](tg://user?id={sysarg})"
    else:
        sysarg = event.pattern_match.group(1)
        user = sysarg
    if sysarg == "":
        await ok.edit(
            "Give me someones id, or reply to somones message to check his/her fedstat."
        )
        return
    else:
        async with borg.conversation(bott) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + sysarg)
                audio = await conv.get_response()
                if "Looks like" in audio.text:
                    await audio.click(0)
                    await asyncio.sleep(2)
                    audio = await conv.get_response()
                    await borg.send_file(
                        event.chat_id,
                        audio,
                        caption=f"List of feds {user} has been banned in.\n\nFSTATS CHECKED BY {LEGENDX} 🔥\n\nCollected by LEGEND BOT.",
                    )
                else:
                    await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await ok.edit("**Error**\n Unblock @MissRose_Bot and try again!")



@borg.on(admin_cmd(pattern="fedinfo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    ok = await event.edit("Extracting information...")
    sysarg = event.pattern_match.group(1)
    async with borg.conversation(bott) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("/fedinfo " + sysarg)
            audio = await conv.get_response()
            await ok.edit(audio.text + "\n\nFedInfo Excracted by LEGENDBOT")
        except YouBlockedUserError:
            await ok.edit("**Error**\n Unblock @MissRose_Bot and try again!")
