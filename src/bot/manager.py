from bot.parameters import Parameters
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, Updater
from logger_handler import get_logger
from bot.commands.help import help_command
import json

_logger = get_logger()

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
        help_handler = CommandHandler('help', help_command, pass_args=True)
        self.dispatcher.add_handler(help_handler)
    
    def start_bot(self):
        """
        It sets up the bot
        """
        self.logger.info('Starting the bot')
        self.updater.start_polling()
        self.updater.idle()

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