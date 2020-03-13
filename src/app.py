import logger_handler
import re
import requests
import logging
from flask import json, request, Flask, jsonify, Response
from bot.manager import Bot_Manager
# Set Flask app
app = Flask(__name__)

# Get Logger
_logger = logger_handler.get_logger()

bot_manager = Bot_Manager()

@app.route('/', methods=['POST', 'GET'])
def call():
    _logger.info("call has been called")
    try:
        if request.method == 'POST':
            msg = request.json
            _logger.info('I received: {}'.format(msg))
            a = bot_manager.add_update(msg)
            _logger.info('After sending a message: {}'.format(a))
            return Response('ok', status=200)
        else:
            return "<h1>Hello bot<h1>"
    except Exception as e:
        _logger.error('Error', exc_info=e)


if __name__ == "__main__":
    app.run(debug=True)