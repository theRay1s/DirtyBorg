"""COMMAND : .balaji"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 15)

    input_str = event.pattern_match.group(1)

    if input_str == "balaji":

        await event.edit(input_str)

        animation_chars = [

            "`Your bot is running\n\nTelethon version:` 1.9.0\n`Python:` 3.7.3\n`User:` @archernap\n`Database Status: Databases functioning normally!`",
            "`Connecting To github.com...`",
            "`Deleting Baalaji Repo....`",
            "`Forking Uniborg... 0%\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 0 MiB / 108.7 MiB`",
            "`Forking Uniborg... 4%\n\n⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 22 MiB / 108.7 MiB`",
            "`Forking Uniborg... 8%\n\n⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 48 MiB / 108.7 MiB`",
            "`Forking Uniborg... 20%\n\n⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 55 MiB / 108.7 MiB`",
            "`Forking Uniborg... 36%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 60 MiB / 108.7 MiB `",
            "`Forking Uniborg... 52%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 90.7 MiB / 108.7 MiB `",
            "`Forking Uniborg... 84%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️\n\nFile Size: 100.7 MiB / 108.7 MiB `",
            "`Forking Uniborg... 100%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️\n\nFile Size: 108.7 MiB / 108.7 MiB\n\nTask Completed... `",
            "`Fork Deploying...`\n\n@UniBorg ( `Custom Built By` @Archer ) \n`Verified Account:` ☑️\n`Official Website:` N/A`Python` `Loading...`\n[GCC 7.4.0]\n`Telethon` `Loading...`\n\n`Custom Built Fork:` `Loading...`",
            "`Fork Deployed...`\n\n@UniBorg ( `Custom Built By` @Archer ) \n`Verified Account:` ✅\n`Official Website:` N/A`Python` 3.7.4 (default, Sep 12 2019, 01:19:52)\n[GCC 7.4.0]\n`Telethon` 1.8.0\n\n`Custom Built Fork:` https://github.com/archertanu/ZenBot"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 15])
