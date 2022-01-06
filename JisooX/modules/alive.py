import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from JisooX.events import register
from JisooX import telethn as tbot


PHOTO = "https://telegra.ph/file/add241c92045b3f359bb3.jpg"

@register(pattern=("/alive"))
async def awake(event):
  PRIME = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm ᴅᴀᴘᴘ ʀʙᴛ.** \n\n"
  PRIME += "✫ **I'm Working Properly** \n\n"
  PRIME += f"✫ **My Lord : [ᴀɴᴀᴋ ᴛᴜʜᴀɴ](https://t.me/SangDappa)** \n\n"
  PRIME += f"✫ **Library Version :** `{telever}` \n\n"
  PRIME += f"✫ **Telethon Version :** `{tlhver}` \n\n"
  PRIME += f"✫ **Pyrogram Version :** `{pyrover}` \n\n"
  PRIME += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/dapprbt_bot?start=help"), Button.url("ʀᴇᴘᴏ​", "https://www.xnxx.com/")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PRIME,  buttons=BUTTON)
