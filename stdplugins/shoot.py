import sys
from telethon import events, functions, __version__
from uniborg.util import admin_cmd
import asyncio


@borg.on(admin_cmd(pattern="shoot$ ?(.*)", allow_sudo=True))  # pylint:disable=E0602
async def killing (killed):
    """ Dont Kill Too much -_-"""
    if not killed.text[0].isalpha() and killed.text[0] not in ("/", "#", "@", "!"):
        if await killed.get_reply_message():
            await killed.edit(
                "Targeted user killed by Headshot 😈......\n"
  "#Sad_Reacts_Onli\n"
            )
