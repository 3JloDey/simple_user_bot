import asyncio

from pyrogram import Client
from pyrogram import filters as F
from pyrogram import idle
from pyrogram.handlers import MessageHandler

from config import load_config
from userbot.handlers.reactions import disrespect
from userbot.handlers.typing import clear_history, slowtyping

USERS = [447938930, 1028068811]

async def main() -> None:
    config = load_config()
    app = Client(
        "my_account",
        api_id=config.user_bot.api_id,
        api_hash=config.user_bot.api_hash,
    )
    
    app.add_handler(MessageHandler(slowtyping, F.me & F.text & F.command("s", ".")))
    app.add_handler(MessageHandler(clear_history, F.me & F.text & F.command("clear", ".")))
    app.add_handler(MessageHandler(disrespect, F.all & F.user(USERS)))

    async with app:
        await idle()


if __name__ == "__main__":
    asyncio.run(main())
