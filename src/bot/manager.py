from bot.parameters import Parameters
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
from logger_handler import get_logger
from queue import Queue
from threading import Thread
from bot.commands.help import help_command
import json

_logger = get_logger()

class Bot_Manager:
    def __init__(self):
        self.parameters = Parameters()
        self.bot = Bot(token=self.parameters.get_token())
        self.set_webhook()
        self.set_dispatcher()
        
    def set_webhook(self):
        webhook_info = self.bot.getWebhookInfo()
        _logger.info(webhook_info)
        if webhook_info['url'] == "":
            self.bot.set_webhook(self.parameters.get_endpoint())
        else:
            pass
    
    def set_dispatcher(self):
        self.update_queue = Queue()
        self.dispatcher = Dispatcher(self.bot, self.update_queue)
        help_handler = CommandHandler('help', help_command, pass_args=True)
        self.dispatcher.add_handler(help_handler)
        thread = Thread(target=self.dispatcher.start, name='dispatcher')
        thread.start()
    
    def add_update(self, update_dict):
        update = self.transcribe_update(update_dict)
        self.update_queue.put(update)
        return 'a'
    
    def transcribe_update(self, update_dict):
        return Update.de_json(update_dict, self.bot)