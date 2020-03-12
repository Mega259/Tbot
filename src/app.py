import logger_handler
import request
import re
import json
import logging
import telegram
from flask import json, request, Flask, jsonify

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


@app.route('/')
def call():
    _logger.info("call has been called")
    try:
        return jsonify({'success': True})
    except Exception as e:
        _logger.error('Error servicio insertRoutes', exc_info=e)

def main():
    # TODO
    
    # 1. Create Basic Flask App
    # 2. Set up a tunnel (Serveo/ngrok)
    # 3. Set a webhook
    # 4. Receive and parse
    # 5. Send Message


if __name__ == "__main__":
    main()
    app.run(debug=True)