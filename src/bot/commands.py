from logger_handler import get_logger
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

logger = get_logger()

def start(update, context):
    logger.info('Called start command')
    keyboard = [[
        InlineKeyboardButton('registrar', callback_data="1"),
        InlineKeyboardButton('help', callback_data="2")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Por favor, elija:', reply_markup=reply_markup)

def button(update, context):
    logger.info('Called button command')
    query = update.callback_query
    query.edit_message_text(text="Opcion seleccionada: {}".format(query.data))

def help_command(update, context):
    logger.info('Called the help command')
    return update.message.reply_text("Hola holita")

def registrar(update, context):
    logger.info('Called the registrar command')
    return update.message.reply_text('Aún no hago nada')
    pass

def error(update, context):
    logger.error('Update {} caused error: {}'.format(update, context.error))