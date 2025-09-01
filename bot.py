from config import API_ID, API_HASH, BOT_TOKEN, SESSION
from pyrogram import Client

# **CRITICAL FIX:** Define the 'user' client at the top level of the file.
# This makes it importable by other files like main.py.
user = Client(
    name="user_session",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="bot_session",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins")
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        self.LOGGER.info(f"Bot started as {self.me.first_name}.")

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot stopped.")

# You can add any other necessary imports or setup here
import logging
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
