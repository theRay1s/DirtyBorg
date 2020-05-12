"""Lydia AI plugin for @UniBorg

.eai <as a reply to user's message //Turns AI on For that user.
.dai <as a reply to user's message //Turns AI off For that user.
.lai // Outputs List Of Currently added Users in AI Auto-Chat.

Description: A module that Act as a chatbot and chat with a User/other Bot.
This Module Needs CoffeeHouse API to work. so Join https://telegram.dog/IntellivoidDev and send #activateapi and follow instructions.
This Module also Needs DB_URI For Storage of Some Data So make sure you have that too.
"""


import coffeehouse as cf

import asyncio
import io
import random
from sql_helpers.lydia_ai_sql import get_s, get_all_s, add_s, remove_s
from time import time
from uniborg.util import admin_cmd

if Config.LYDIA_API is not None:
    api_key = Config.LYDIA_API
    # Initialise client
    api_client = cf.API(api_key)


@borg.on(admin_cmd(pattern="(e|d|l)ai", allow_sudo=True))
async def lydia_disable_enable(event):
    if event.fwd_from:
        return
    if Config.LYDIA_API is None:
        await event.edit("please add required `LYDIA_API` env var")
        return
    if event.reply_to_msg_id is not None:
        input_str = event.pattern_match.group(1)
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.from_id
        chat_id = event.chat_id
        await event.edit("hi")
        if input_str == "e":
            session = api_client.create_session()
            logger.info(session)
            logger.info(add_s(user_id, chat_id, session.id, session.expires))
            await event.edit(f"Hi, How are you")
        elif input_str == "d":
            logger.info(remove_s(user_id, chat_id))
            await event.edit(f"[Bye, have to go...](tg://user?id={user_id})")
        elif input_str == "l":
            lsts = get_all_s()
            if len(lsts) > 0:
                output_str = "AI enabled users:\n\n"
                for lydia_ai in lsts:
                    output_str += f"[user](tg://user?id={lydia_ai.user_id}) in chat `{lydia_ai.chat_id}`\n"
            else:
                output_str = "no Lydia AI enabled users / chats. Start by replying `.enacf` to any user in any chat!"
            if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
                with io.BytesIO(str.encode(output_str)) as out_file:
                    out_file.name = "@r4v4n4_lydia_ai.text"
                    await borg.send_file(
                        event.chat_id,
                        out_file,
                        force_document=True,
                        allow_cache=False,
                        caption="Lydia AI enabled users",
                        reply_to=event
                    )
            else:
                await event.edit(output_str)
        else:
            await event.edit("Reply To User Message to Add / Delete them from Lydia Auto-Chat.")
    else:
        await event.edit("Reply To A User's Message to Add / Delete them from Lydia Auto-Chat.")


@borg.on(admin_cmd(incoming=True))
async def on_new_message(event):
    if event.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if Config.LYDIA_API is None:
        return
    if not event.media:
        user_id = event.from_id
        chat_id = event.chat_id
        s = get_s(user_id, chat_id)
        if s is not None:
            session_id = s.session_id
            session_expires = s.session_expires
            query = event.text
            # Check if the session is expired
            # If this method throws an exception at this point,
            # then there's an issue with the API, Auth or Server.
            if session_expires < time():
                # re-generate session
                session = api_client.create_session()
                logger.info(session)
                session_id = session.id
                session_expires = session.expires
                logger.info(add_s(user_id, chat_id, session_id, session_expires))
            # Try to think a thought.
            try:
                async with event.client.action(event.chat_id, "typing"):
                    await asyncio.sleep(random.randint(0, 6))
                    output = api_client.think_thought(session_id, query)
                    await event.reply (output)
            except cf.exception.CoffeeHouseError as e:
                logger.info(str(e))
