import os
import logging
from pyrogram import Client

# --- Configuration ---
# Load environment variables directly to avoid import errors.
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SESSION = os.environ.get("SESSION")
# Using OWNER_ID as you originally had it.
OWNER_ID = int(os.environ.get("OWNER_ID"))

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

# --- Client Definitions ---
# Define the 'user' client at the top level to make it importable.
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
