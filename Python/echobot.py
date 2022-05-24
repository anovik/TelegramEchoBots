#!/usr/bin/env python

import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hello, write any message and echo bot will answer you!')


def help(update, context):    
    update.message.reply_text('Help!')


def echo(update, context):    
    update.message.reply_text(update.message.text)


def error(update, context):    
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():    
    # Get token from os settings
    TELEGRAM_ECHO_TOKEN = os.getenv('TELEGRAM_ECHO_TOKEN')

    # Create the Updater and pass it your bot's token.
    updater = Updater(TELEGRAM_ECHO_TOKEN, use_context=True)
    
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
 
    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C 
    updater.idle()


if __name__ == '__main__':
    main()
