import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Jebot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Jebot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Hey There, I'm Telegraph Bot

I can upload photos or videos to telegraph. Made by @tobot_update 🇱🇰

Click /help to find out more about how to use me</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "CHANNEL📢", url="https://t.me/tobot_update"),
                                        InlineKeyboardButton(
                                            "GROUP👥", url="https://t.me/tobotupdate")
                                    ],[
                                      InlineKeyboardButton(
                                            "DEVLOAPER👩‍💻", url="https://t.me/rungram")
                                      InlineKeyboardButton(
                                            "REPO🤖", url="https://t.me/bot_repo")
                                    ],[
                                      Inlinekeyboardbutton(
                                            "🔔SUBSCRIBE🔔", url="https://youtube.com/channel/UC1SeMwgyNDi_n4T8cbgVjKQ")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Telegraph Bot Help!

Just send a photo or video less than 5mb file size, I'll upload it to telegraph.

~ @TOBOT_UPDATE</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back🔙", callback_data="start"),
                                        InlineKeyboardButton(
                                            "About📝", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "CHANNEL📢", url="https://t.me/tobot_update")
                                        Inlinekeyboardbutton(
                                            "GROUP👥", url="https://t.me/tobotupdate")
                                  ],[
                                        Inlinekeyboardbutton(
                                            "🔔SUBSCRIBE🔔", url="https://youtube.com/channel/UC1SeMwgyNDi_n4T8cbgVjKQ")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>About Telegraph Bot!</b>

<b> Developer👩‍💻:</b> <a href="https://t.me/rungram">RUNGRAM 🇱🇰</a>

<b> CHANNEL📢:</b> <a href="https://t.me/tobot_update">TOBOT UPDATE</a>

<b> GROUP👥:</b> <a href="https://t.me/tobotupdate">JOIN</a>

<b> REPO🤖:</b> <a href="https://t.me/bot_repo">CODE</a>

<b> 🔔SUBSCRIBE🔔:</b> <a href="https://youtube.com/channel/UC1SeMwgyNDi_n4T8cbgVjKQ">SUBSCRIBE</a>

<b>~ BY @tobot_update</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back🔙", callback_data="help"),
                                        InlineKeyboardButton(
                                            "CHANNEL📢", url="https://t.me/tobot_update")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Photo size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\nJoin @TOBOT_UPDATE**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Jebot.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Video size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\nJoin @TOBOT_UPDATE**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Jebot.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Gif size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\nJoin @TOBOT_UPDATE**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Jebot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

print(
    """
Bot Started!
Join @TOBOT_UPDATE
"""
)

Jebot.run()
