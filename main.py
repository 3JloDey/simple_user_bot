import asyncio
# import uvloop

from pyrogram import Client
from pyrogram import filters as F
from pyrogram import idle
from pyrogram.handlers import MessageHandler
from pyrogram.enums import ParseMode

from config import load_config
from userbot.handlers.send_voice import send_tinkoff_voice
from userbot.handlers.clear_history import clear_message_history
from userbot.handlers.slow_type import slowtyping
from userbot.handlers.search_in_google import google_search


INFO ="""Для медленной печати введите <code>/s текст</code>
\nДля очистки <b>вашей</b> истории сообщений введите <code>/clear</code>\n
Триггер слова для Олега Тинькова: заебись, пиздец, прихерел, выродок, похуй, говно, сомнительно"""

async def main() -> None:
    config = load_config()
    # uvloop.install()
    app = Client(
        "my_account",
        api_id=config.user_bot.api_id,
        api_hash=config.user_bot.api_hash,
        parse_mode=ParseMode.HTML
    )
    
    app.add_handler(MessageHandler(slowtyping, F.me & F.command("s")))
    app.add_handler(MessageHandler(clear_message_history, F.me & F.command("clear")))
    app.add_handler(MessageHandler(google_search, F.me & F.command("google")))
    app.add_handler(MessageHandler(send_tinkoff_voice, F.me))
    

    async with app:
        await app.send_message(chat_id="me", text=f"Бот запущен 😇\n{INFO}")
        await idle()


if __name__ == "__main__":
    # uvloop.install()
    asyncio.run(main())
