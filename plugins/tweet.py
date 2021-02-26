#tweet made for ultroid x


"""
✘ Commands Available -

• `{i}tweet`
    make twitter posts.

"""

from . import *
from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError


@ultroidx_cmd(pattern="tweet ?(.*)")
async def tweet(e):
    wai = await eor(e,"processing...")
    text = e.pattern_match.group(1)
    try:
        results = await ultroid_bot.inline_query(
            "twitterstatusbot",text
        )
        await results[0].click(
            e.chat_id,
            silent=True,
            hide_via=True,
        )
        await wai.delete()
    except ChatSendInlineForbiddenError:
        await wai.edit("`Boss ! I cant use inline things here...`")
    except ChatSendStickersForbiddenError:
        await wai.edit("Sorry boss, I can't send Sticker Here !!")
        
HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
