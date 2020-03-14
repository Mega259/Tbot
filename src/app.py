import logger_handler
from bot.manager import Bot_Manager

# Get Logger

# bot_manager = Bot_Manager()

# @app.route('/', methods=['POST', 'GET'])
# def call():
#     _logger.info("call has been called")
#     try:
#         if request.method == 'POST':
#             msg = request.json
#             _logger.info('I received: {}'.format(msg))
#             a = bot_manager.add_update(msg)
#             _logger.info('After sending a message: {}'.format(a))
#             return Response('ok', status=200)
#         else:
#             return "<h1>Hello bot<h1>"
#     except Exception as e:
#         _logger.error('Error', exc_info=e)

def start_bot():
    logger = logger_handler.set_logger()
    bot_manager = Bot_Manager(logger)
    bot_manager.start_bot()

if __name__ == "__main__":
    start_bot()