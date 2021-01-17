from aiogram.utils.executor import start_webhook
from loader import bot
from config import WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_PATH, WEBHOOK_URL


async def on_startup(dp):
    await bot.set_webhook(
        url=WEBHOOK_URL,
    )



if __name__ == '__main__':
    from handlers import dp

    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )