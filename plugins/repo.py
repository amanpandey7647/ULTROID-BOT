"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))

                 MADE BY LEGENDX22
                 IDEA BY PROBOY22
                 CREDITS TEAMLEGEND
                 PLEASE KEEP CREDITS 🥺
"""
from LEGEND import admin_cmd


@bot.on(admin_cmd(outgoing=True, pattern="repo"))
async def repo(event):
    if event.fwd_from:
        return
    LEGENDX = Var.BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(LEGENDX, "repo")
    await response[0].click(event.chat_id)
    await event.delete()


"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
"""



BOT = "ULTROID"
from telethon import events, Button, custom
import os,re
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
@tgbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):
 LEGEND = event.builder
 X= [[custom.Button.inline("🔥 CLICK ME 🔥",data="obhai")]]
 query = event.text
 result = LEGEND.article("LEGEND",text="REPO AND SUPPORT",buttons=X,link_preview=False)
 await event.answer([result])
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
async def callback_query_handler(event):

# inline by LEGENDX22 and PROBOY22 🔥
  await event.edit(text=f"{BOT} REPO AND GROUP LINK",buttons=[[Button.url(f"🔥{BOT} REPO🔥", url="http://github.com/ULTROID-OP/ULTROID-BOT"), Button.url(f"⚡{BOT} SUPPORT⚡", url="https://t.me/ULTROID_OP")]])
