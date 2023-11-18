import asyncio
import re

from pyrogram import Client
from pyrogram.enums import ChatAction
from pyrogram.errors import FloodWait
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
            await asyncio.sleep(0.05)

            to_edit += text[0]
            text = text[1:]

            await message.edit(to_edit)
            await asyncio.sleep(0.05)

        except FloodWait as e:
            await asyncio.sleep(e.value)


async def clear_history(client: Client, message: Message) -> None:
    try:
        limit = int(message.text.strip(".clear") or "0")

        async for msg in client.get_chat_history(chat_id=message.chat.id, limit=limit):
            if msg.from_user is not None and (msg.from_user.id == client.me.id):
                await msg.delete()
    except ValueError:
        await message.delete()