import asyncio
import re

import emoji
from pyrogram import Client
from pyrogram.enums import ChatAction
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import ReactionInvalid
from pyrogram.types import Message


async def slowtyping(client: Client, message: Message) -> None:
    clear_message = re.sub(r"^\s*\.s\s*", "", message.text)
    text = clear_message
    to_edit = ""
    symbol = "█"

    while to_edit != clear_message:
        await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
        try:
            await message.edit(to_edit + symbol)
            await asyncio.sleep(0.08)

            to_edit += text[0]
            text = text[1:]

            await message.edit(to_edit)
            await asyncio.sleep(0.08)

        except FloodWait as e:
            await asyncio.sleep(e.value)


async def clear_history(client: Client, message: Message) -> None:
    try:
        limit = int(message.text.strip(".clear") or "0")

        async for msg in client.get_chat_history(chat_id=message.chat.id):
            if msg.from_user is not None and (msg.from_user.id == client.me.id):
                await msg.delete()
    except ValueError:
        await message.delete()


async def react_all_messages(client: Client, message: Message) -> None:
    await message.delete()

    data = message.text.split()
    if len(data) > 1 and message.reply_to_message:
        _, char = data

        target_user_id = message.reply_to_message.from_user.id
        chat_id = message.chat.id

        async for msg in client.get_chat_history(chat_id):
            if msg.from_user and msg.from_user.id == target_user_id:
                try:
                    await client.send_reaction(chat_id=chat_id, message_id=msg.id, emoji=char)

                except FloodWait as e:
                    await asyncio.sleep(e.value)

                except ReactionInvalid:
                    if emoji.is_emoji(char):
                        await client.send_reaction(chat_id=chat_id, message_id=msg.id)
                        await client.send_reaction(chat_id=chat_id, message_id=msg.id, emoji=char)
