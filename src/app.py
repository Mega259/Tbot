import logger_handler
import re
import requests
import json
import logging
import telegram
from flask import json, request, Flask, jsonify, Response

# Set Flask app
app = Flask(__name__)

# Get Logger
_logger = logger_handler.get_logger()

# Read access_data
with open('access_data.json', 'r') as f:
    access_data = json.load(f) 

bot_token = access_data['token']
bot_user_name = access_data['user_name']

bot = telegram.Bot(token=bot_token)
_logger.info(bot.get_me())


@app.route('/', methods=['POST', 'GET'])
def call():
    _logger.info("call has been called")
    try:
        if request.method == 'POST':
            msg = request.json
            _logger.info('I received: {}'.format(msg))
            return Response('ok', status=200)
        else:
            return "<h1>Hello bot<h1>"
    except Exception as e:
        _logger.error('Error', exc_info=e)

def set_webhook(url):
    pass

def main():
    # TODO
    
    # 1. Create Basic Flask App
    # 2. Set up a tunnel (Serveo/ngrok)
    # 3. Set a webhook # https://api.telegram.org/bot{}/setWebhook?url={}
    # 4. Receive and parse
    # 5. Send Message
    pass

if __name__ == "__main__":
    app.run(debug=True)