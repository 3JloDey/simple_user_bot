from pyrogram import Client
from pyrogram.types import Message


async def clear_message_history(client: Client, message: Message) -> None:
    async for msg in client.get_chat_history(chat_id=message.chat.id):
        if msg.from_user is not None and (msg.from_user.id == client.me.id):
            await msg.delete()
