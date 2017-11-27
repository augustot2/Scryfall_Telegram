import logging
import json
import os
import sys

from cloudfn.http import handle_http_event, Response
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, InlineQueryHandler

import scryfall_telegram.actions as actions
import scryfall_telegram.hooks


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)
log.info("Bot starting!")

with open(os.path.join(os.path.dirname(sys.executable), 'token.txt')) as f:
    token = f.read().strip()
bot = Bot(token)

#with open(os.path.join(os.path.dirname(sys.executable), 'endpoint.txt')) as f:
#    endpoint = f.read().strip()
#bot.set_webhook(endpoint)

dispatcher = Dispatcher(bot, None, workers=0)

dispatcher.add_handler(CommandHandler('start', actions.start))
dispatcher.add_handler(InlineQueryHandler(actions.inline_search))


def handle_http(req):
    global bot, dispatcher

    update = Update.de_json(json.loads(req.body), bot)
    dispatcher.process_update(update)

    return Response(
        status_code=200
    )


handle_http_event(handle_http)
