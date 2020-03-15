from bot.parameters import Parameters
from telegram import Bot, Update, ReplyKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, Updater, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
from logger_handler import get_logger
from bot.commands import start, button, help_command, error
import json, logging
import os
class Bot_Manager:
    def __init__(self, logger):
        """
        Creator of class Bot_Manager
        
        Parameters
        ----------
        logger : A logging object
        """
        self.logger = logger
        self.parameters = Parameters()
        self.set_bot()
    
    def set_bot(self):
        """
        It sets up the bot
        """
        self.logger.info('Setting up Bot')
        self.bot = Bot(token=self.parameters.get_token())
        self.logger.info('Setting up the udater and the dispatcher')
        self.set_updater_and_dispatcher()
    
    def set_updater_and_dispatcher(self):
        """
        It sets up the updater and dispatcher
        """
        self.updater = Updater(self.parameters.get_token(), use_context=True)
        self.dispatcher = self.updater.dispatcher
        start_handler = CommandHandler('start', start, pass_args=True)
        help_handler = CommandHandler('help', help_command, pass_args=True)
        self.dispatcher.add_handler(help_handler)
        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(CallbackQueryHandler(button))
        self.dispatcher.add_error_handler(error)
        self.dispatcher.add_handler(setup_registrar_handler())

    def start_bot(self):
        """
        It sets up the bot
        """
        self.logger.info('Starting the bot')
        self.updater.start_polling()
        self.updater.idle()

#### FUNTIONS
path = os.path.abspath(os.path.dirname(__file__))
users = os.path.join(path, 'users.json')
CHOOSING, TYPING_CHOICE = range(2)

def setup_registrar_handler():
    ##CHOOSING, TYPING_REPLY = range(2)
    return ConversationHandler(
        entry_points=[CommandHandler('registrar', start_registrar)],

        states={
            CHOOSING: [MessageHandler(Filters.regex('^(Nombre completo|Mes de pago|Grupo de trabajo)$'), generic_choice),
                       MessageHandler(Filters.regex('^(Acabar)$'), done)],
            TYPING_CHOICE: [MessageHandler(Filters.text, received_information)]
        },

        fallbacks=[MessageHandler(Filters.regex('^SI$'), done)]
    )

reply_keyboard = [
    ['Nombre completo', 'Mes de pago'],
    ['Grupo de trabajo'],
    ['Acabar']
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

def start_registrar(update, context):
    user_id = update.message.chat.username
    try:
        with open(users, 'r') as f:
            a = json.load(f)
            try:
                context.user_data.update(a[user_id])
            except Exception as e:
                pass
            f.close()
        if (len(context.user_data) != 0):
            update.message.reply_text('Bienvenido de nuevo, ¿qué dato deseas editar?', reply_markup=markup)
        else:
            update.message.reply_text(
                "Hola, soy Wallee, el bot del FABLAB Badajoz "
                "Vamos a proceder a registrarte",
                reply_markup=markup)
    except Exception as e:
        print(e)
    return CHOOSING

def generic_choice(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    if (text == 'Nombre completo'):
        update.message.reply_text('Escriba su nombre completo a continuación:')
    elif (text == 'Mes de pago'):
        update.message.reply_text('Escriba el mes de pago de la cuota anual:')    
    elif (text == 'Grupo de trabajo'):
        update.message.reply_text('Escriba su grupo u grupos de trabajo separados por coma:')

    return TYPING_CHOICE

def received_information(update, context):
    user_data = context.user_data
    text = update.message.text
    category = user_data['choice']
    user_data[category] = text
    
    #update.message.reply_text("Bien!! Por ahora tenemos esto:"
    #                            "{} .Continuemos..." .format(facts_to_str(user_data)),
    #                            reply_markup=markup)
    
    if (category == 'Nombre completo'):
        update.message.reply_text('Bien!! Su nombre es: {}. \n'
                                    'Vuelva a elegir o pulse acabar'.format(text),
                                    reply_markup=markup)
    elif (category == 'Mes de pago'):
        update.message.reply_text('Genial!! El mes de pago de tu cuota fue en: {}. \n'
                                    'Vuelva a elegir o pulse acabar'.format(text),
                                    reply_markup=markup)    
    elif (category == 'Grupo de trabajo'):
        update.message.reply_text('Perfecto!! Tus grupos de trabajo son: '
                                    '{}.\n Vuelva a elegir o pulse acabar' .format(facts_to_str(user_data)),
                                    reply_markup=markup)
        
    del user_data['choice']

    return CHOOSING
    

def done(update, context):
    user_data = context.user_data
    user_id = update.message.chat.username
    print(user_data)
    if 'choice' in user_data:
        del user_data['choice']
    db = {}
    with open(users, 'r') as f:
        db = json.load(f)
        if user_id in db:
            print('Antes de sobreescribir')
            db[user_id] = user_data
        else:
            print('Antes de escribir escribir')
            db.update({user_id: user_data})
        print('Terminando escribir')
        f.close()
    with open(users, 'w') as f:
        json.dump(db, f, default=str)
        f.close()
    update.message.reply_text("Felicidades!! El registro se ha completado correctamente...")
    user_data.clear()
    return ConversationHandler.END


def facts_to_str(user_data):
    facts = list()
    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))
    return "\n".join(facts).join(['\n', '\n'])

    # Old Code
    # def set_webhook(self):
    #     """   
    #     It sets up a webhook
    #     """
    #     webhook_info = self.bot.getWebhookInfo()
    #     _logger.info(webhook_info)
    #     if webhook_info['url'] != self.parameters.get_endpoint():
    #         self.bot.set_webhook(self.parameters.get_endpoint())
    #     else:
    #         pass
    
    
    # def set_dispatcher(self):
    #     self.update_queue = Queue()
    #     self.dispatcher = Dispatcher(self.bot, self.update_queue)
    #     help_handler = CommandHandler('jiji', help_command, pass_args=True)
    #     self.dispatcher.add_handler(help_handler)
    #     thread = Thread(target=self.dispatcher.start, name='dispatcher')
    #     thread.start()
    # def main(self):
    #     self.updater = Updater(self.parameters.get_token(), use_context=True)
    #     self.dp = updater.dispatcher
    #     help_handler = CommandHandler('help', help_command)
    #     dp.add_handler(help_handler)
    
    # def add_update(self, update_dict):
    #     update = self.transcribe_update(update_dict)
    #     self.update_queue.put(update)
    #     return 'a'
    
    # def transcribe_update(self, update_dict):
    #     return Update.de_json(update_dict, self.bot)