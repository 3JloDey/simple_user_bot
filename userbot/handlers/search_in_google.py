from googleapi import google
from pyrogram import Client
from pyrogram.types import Message


async def google_search(client: Client, message: Message) -> None:
    if message.reply_to_message:
        text = message.text.split()[1:]
        if text:
            search_results = google.search(text, 1)
            links = []
            for result in search_results:
                links.append(result.links)
            
            links_to_str = "\n".join(links)    
            await client.send_message(chat_id=message.chat.id,
                                        text=f'Почитай тут\n{links_to_str}',
                                        reply_to_message_id=message.reply_to_message.id)