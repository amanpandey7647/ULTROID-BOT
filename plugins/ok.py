from LEGEND import admin_cmd
@bot.on(admin_cmd("huh ?(.*)"))
async def hehe(event):
  await event.edit("your bot is updated successfully")
