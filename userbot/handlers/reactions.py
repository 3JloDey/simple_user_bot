import asyncio

from pyrogram import Client
from pyrogram.types import Message


async def disrespect(client: Client, message: Message) -> None:
    await asyncio.sleep(4.5)
    await client.send_reaction(message.chat.id, message.id, "🤡")
