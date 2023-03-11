from os import environ
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(environ.get("APP_ID", "14082290")),
    api_hash= environ.get("API_HASH", "ef7c8ee7f5a019ccca3f28d441d3bc49"),
    bot_token= environ.get("TOKEN", "5913677128:AAGtYlFw83PLrb1eAJfPCnOm4C7ICKYxaek")
)
