import ssl
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN, WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV

bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
SSL_CERTIFICATE = open(WEBHOOK_SSL_CERT, "rb").read()
ssl_context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV)