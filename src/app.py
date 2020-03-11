import logger_handler
import request
import re
import json
import logging
import telegram
# Get Logger
logger_handler.set_logger()

_logger = logger_handler.get_logger()

# Read access_data
with open('access_data.json', 'r') as f:
    access_data = json.load(f) 

bot_token = access_data['token']
bot_user_name = access_data['user_name']

bot = telegram.Bot(token=bot_token)
_logger.info(bot.get_me())