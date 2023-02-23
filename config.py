#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5761014459:AAFi_2AK1x0xNjWhatqabahETR3ftzlipzQ")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "9277175"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "0c232abc4358fe3f0e2666a945654793")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "AgCNjvcAsq1yURbqSYuUdXA2AJdN8V5ayXvFClaNrX21D6_H6Zaz-H02a1J26ufXRV693etrsbpSUUJ44UHvUChs7zSTRvIL9diibOidl9g3Tp87mIffU2WINiZIRzAUUALp08P45FnIaoFNA0JIG4gCDO66I4kS4Pq8G_3QVm9hDQ6--qdfARNvW3UFj-ESdREXENpd-318yjLGPoDNS8kEKE0no5TtpMVOZO4zYgzU-evJLLjKBPcut8NPa7wD6aAjGIWUr7k6UlJoO61KXOXKQhjlpqUSvXWxKjkKn4bVmJhbAIyB1JkvCAC6HAJ0OyIKuguUiCxypEDEBwkBfWfj3jPm3gAAAAEyrw1MAA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://howtodotech:howtodotech@cluster0.vxo1wqs.mongodb.net/?retryWrites=true&w=majority")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
