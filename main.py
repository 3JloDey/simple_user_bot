from pyrogram import Client, filters
from pyrogram.types import Message

from .config import load_config

config = load_config()
app = Client(
    "my_account",
    api_id=config.user_bot.api_id,
    api_hash=config.user_bot.api_hash,
)


@app.on_message(filters.all & filters.user(1028068811))
async def daun_disrespect(client: Client, message: Message) -> None:
    await app.send_reaction(message.chat.id, message.id, "🤡")


app.run()
