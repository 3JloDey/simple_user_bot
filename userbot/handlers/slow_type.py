import time
import re

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.enums import ChatAction
from pyrogram.errors import FloodWait

async def slowtyping(client: Client, message: Message) -> None:
    clear_message = re.sub(r"^\s*\/s\s*", "", message.text)
    text = clear_message
    to_edit = ""
    symbol = "█"

    while to_edit != clear_message:
        await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
        try:
            await message.edit(to_edit + symbol)
            time.sleep(0.05)

            to_edit += text[0]
            text = text[1:]

            await message.edit(to_edit)
            time.sleep(0.05)

        except FloodWait as e:
            await time.sleep(e.value)