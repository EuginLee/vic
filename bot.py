 


TOKEN = '1197056727:AAFeVAmjnp-XW74roTXsorfkXwNwzVIUVEk'


"""
Simple Bot to reply to Telegram messages taken from the python-telegram-bot examples.
Deployed using heroku.
Author: liuhh02 https://medium.com/@liuhh02
"""

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
import os

# from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext.dispatcher import run_async
import requests
import re
import random

PORT = int(os.environ.get('PORT', 5000))

TOKEN = '1197056727:AAFeVAmjnp-XW74roTXsorfkXwNwzVIUVEk'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('WooF!!')

def get_url():
    contents = requests.get('https://dog.ceo/api/breed/pembroke/images/random').json()
    url = contents['message']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

@run_async
def bop(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def come(update, context):
    urls = ["https://media.giphy.com/media/vGo2sgzeC8r60/giphy.gif",\
            "https://media.giphy.com/media/RuP38JSfj14je/giphy.gif",\
            "https://media.giphy.com/media/8Bbl0U61TN6DK/giphy.gif",\
            "https://media.giphy.com/media/eeUJaTwsHh3tswkaYm/giphy.gif",\
            "https://media.giphy.com/media/ITMf6qQnqNLFu/giphy.gif",\
            "https://media.giphy.com/media/rcw4NNFE6JioM/giphy.gif",\
            "https://media.giphy.com/media/WAkTocsutMLrG/giphy.gif"]
    url = random.choice(urls)
    chat_id = update.message.chat_id
    context.bot.send_animation(chat_id=chat_id, animation=url)

def play(update, context):
    urls = ["https://media.giphy.com/media/kgKo71L43f85O/giphy.gif",\
            "https://media.giphy.com/media/7jsnB2RRzDGIo/giphy.gif",\
            "https://media.giphy.com/media/7NUdxH6uzeI1i/giphy.gif",\
            "https://media.giphy.com/media/bWS1Vh9mVkcZq/giphy.gif",\
            "https://media.giphy.com/media/ZjUjG4xgRiSOc/giphy.gif" ]
    url = random.choice(urls)
    chat_id = update.message.chat_id
    context.bot.send_animation(chat_id=chat_id, animation=url)

def wdab(update, context):
    urls = ["https://media.giphy.com/media/mP94uHyKvY1nq/giphy.gif",\
            "https://media.giphy.com/media/xT9IgpxorXdkhoQle8/giphy.gif",\
            "https://media.giphy.com/media/GUx4WVQJLESaI/giphy.gif",
            "https://media.giphy.com/media/l0Nwz1ehUndfqL9MQ/giphy.gif",\
            "https://media.giphy.com/media/3oKIPvl6VJA7wHzIFa/giphy.gif"\
            "https://media.giphy.com/media/KY3VnTOONvgxllVac0/giphy.gif"\
            "https://media.giphy.com/media/L3K0C906B21wY/giphy.gif"\
            "https://media.giphy.com/media/WRWykrFkxJA6JJuTvc/giphy.gif"\
            "https://media.giphy.com/media/dXckBa1HDG86RqUh19/giphy.gif"\
            "https://media.giphy.com/media/THXT0zOw7j7si9PYPS/giphy.gif"
             ]
    url = random.choice(urls)
    chat_id = update.message.chat_id
    context.bot.send_animation(chat_id=chat_id, animation=url)

# def help(update, context):
#     """Send a message when the command /help is issued."""
#     update.message.reply_text('Help!')

# def echo(update, context):
#     """Echo the user message."""
#     update.message.reply_text(update.message.text)

# def error(update, context):
#     """Log Errors caused by Updates."""
#     logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    #dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler('woof',bop))
    dp.add_handler(CommandHandler('come',come))
    dp.add_handler(CommandHandler('play',play))
    dp.add_handler(CommandHandler('wdab',wdab))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    #dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://stormy-stream-53137.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()




# from telegram.ext import Updater, InlineQueryHandler, CommandHandler
# from telegram.ext.dispatcher import run_async
# import requests
# import re

# def get_url():
#     contents = requests.get('https://dog.ceo/api/breed/pembroke/images/random').json()
#     url = contents['message']
#     return url

# def get_image_url():
#     allowed_extension = ['jpg','jpeg','png']
#     file_extension = ''
#     while file_extension not in allowed_extension:
#         url = get_url()
#         file_extension = re.search("([^.]*)$",url).group(1).lower()
#     return url

# @run_async
# def bop(update, context):
#     url = get_image_url()
#     chat_id = update.message.chat_id
#     context.bot.send_photo(chat_id=chat_id, photo=url)

# def main():
#     updater = Updater(TOKEN, use_context=True)
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler('bop',bop))
#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()
