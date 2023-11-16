import asyncio

from pyrogram import Client
from pyrogram import filters as F
from pyrogram import idle
from pyrogram.handlers import MessageHandler

from config import load_config
from userbot.handlers.clown_reaction import disrespect
from userbot.handlers.slowtyping import typing


async def main() -> None:
    config = load_config()
    app = Client(
        "my_account",
        api_id=config.user_bot.api_id,
        api_hash=config.user_bot.api_hash,
    )

    app.add_handler(MessageHandler(typing, F.me & F.text & F.command("t", ".")))
    app.add_handler(MessageHandler(disrespect, F.all & F.user(1028068811)))

    async with app:
        await idle()


if __name__ == "__main__":
    asyncio.run(main())
