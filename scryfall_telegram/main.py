import logging
import json
import os
import sys

from telegram.ext import Updater, Dispatcher, CommandHandler, InlineQueryHandler

import scryfall_telegram.actions as actions
import scryfall_telegram.hooks


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)
log.info("Bot starting!")

TOKEN = os.getenv("TELEGRAM_TOKEN")
PORT = int(os.environ.get('PORT', '5000'))
APPNAME = 'pure-beyond-46891'

updater = Updater(TOKEN)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', actions.start))
dispatcher.add_handler(InlineQueryHandler(actions.inline_search))

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook(f"https://{APPNAME}.herokuapp.com/{TOKEN}")
updater.idle()
