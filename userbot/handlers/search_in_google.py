from googlesearch import search
from pyrogram import Client
from pyrogram.types import Message


async def google_search(client: Client, message: Message) -> None:
    await message.delete()
    text = message.text.split()[1:]
    query = " ".join(text)
    if message.reply_to_message:
        query = message.reply_to_message.text  
        
    if query:
        for url in search(query, stop=1):
            if message.reply_to_message:
                await client.send_message(chat_id=message.chat.id,
                                        text=f"Результат поиска по запросу...\n"
                                            f"[{message.reply_to_message.text}]({url})",
                                        reply_to_message_id=message.reply_to_message.id,
                                        disable_web_page_preview=True)
            else:
                await client.send_message(chat_id=message.chat.id,
                                        text=f'Окей, я погуглил:\n[{query}]({url})',
                                        disable_web_page_preview=True)