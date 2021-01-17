import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
GROUP = -1001174270375
CHANNEL = -1001192452794

WEBHOOK_HOST = "https://talimlinkbot.herokuapp.com"
WEBHOOK_PORT = 8443
WEBHOOK_PATH = f"/bot/{TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '0.0.0.0'  # or ip
WEBAPP_PORT = int(os.getenv('PORT'))
