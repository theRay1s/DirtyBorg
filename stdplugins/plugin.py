"""Emoji

Available Commands:

.install"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "install":

        await event.edit(input_str)

        animation_chars = [
        
            "`Downloading Plugin..`",
            "`Downloading Plugin....`",
            "`Uploading To GitHub\nLoading... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Uploading To GitHub\nLoading... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Uploading To GitHub\nLoading... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Uploading To GitHub\nLoading... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Uploading To GitHub\nLoading... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Uploading To GitHub\nLoading... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Uploading To GitHub\nLoading... 84%\n█████████████████████▒▒▒▒ `",
            "`Uploading To GitHub\nLoading... 100%\n█████████████████████████ `",
            "`Plugin Uploaded To GitHub...\n\nRun Your Installed Plugin With Correct Trigger...`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
