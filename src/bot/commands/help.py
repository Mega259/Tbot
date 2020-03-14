# Command help
from logger_handler import get_logger

logger = get_logger()
def help_command(update, context):
    logger.info('Called the help command')
    return update.message.reply_text("Use /start to test this bot.")
