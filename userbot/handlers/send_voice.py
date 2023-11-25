from pyrogram import Client
from pyrogram.enums import ChatAction
from pyrogram.types import Message

VOICES = {
    "заебись": r".\voices\zaebis.mp3",
    "пиздец": r".\voices\pizdec.mp3",
    "прихерел": r".\voices\priherel.mp3",
    "выродок": r".\voices\virodok.mp3",
    "похуй": r".\voices\pohyu.mp3",
    "говно": r".\voices\govno.mp3",
    "сомнительно": r".\voices\somnitelno.mp3",
}


async def send_tinkoff_voice(client: Client, message: Message) -> None:
    data = message.text.lower().split()
    if len(data) > 0:
        voice = VOICES.get(data[0])
        if voice is not None:
            await client.send_chat_action(
                chat_id=message.chat.id, action=ChatAction.RECORD_AUDIO
            )
            await message.delete()
            if message.reply_to_message:
                await client.send_voice(
                    chat_id=message.chat.id,
                    voice=voice,
                    reply_to_message_id=message.reply_to_message.id,
                )
            else:
                await client.send_voice(chat_id=message.chat.id, voice=voice)
