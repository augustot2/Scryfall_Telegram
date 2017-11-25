from telegram.bot import Bot
from telegram.update import Update
from telegram import InlineQueryResultArticle, InputTextMessageContent

import scryfall_telegram.scryfall as scryfall
import scryfall_telegram.parsers as parse


def start(bot: Bot, update: Update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Welcome to the Scryfall bot!")


def inline_search(bot: Bot, update: Update):
    query = update.inline_query.query
    if not query:
        return

    results = scryfall.cards_search(query)
    items = parse.cards_to_articles(results)[1:50]

    bot.answer_inline_query(update.inline_query.id, items)
