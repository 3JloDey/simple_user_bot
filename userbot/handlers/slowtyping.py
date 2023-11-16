import asyncio
import re

from pyrogram import Client
from pyrogram.errors import FloodWait
from pyrogram.types import Message


async def typing(client: Client, message: Message) -> None:
    clear_message = re.sub(r"^\s*\.t\s*", "", message.text)
    text = clear_message
    to_edit = ""
    symbol = "█"

    while to_edit != clear_message:
        try:
            await message.edit(to_edit + symbol)
            await asyncio.sleep(0.05)

            to_edit += text[0]
            text = text[1:]

            await message.edit(to_edit)
            await asyncio.sleep(0.05)

        except FloodWait as e:
            await asyncio.sleep(e.value)
