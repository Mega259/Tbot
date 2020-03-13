# Command help
import json

def help_command(update, context):
    with open('update.json', 'w+') as f:
        json.dump(update, f, default=str)
    with open('context.json', 'w+') as g:
        json.dump(context, g, default=str)
    return context.bot.send_message('Por ahora no hago mucho', chat_id=context.message.chat.id)