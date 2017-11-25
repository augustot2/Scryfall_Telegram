import logging

from telegram.ext import Updater, CommandHandler, InlineQueryHandler

import scryfall_telegram.actions as actions


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main():
    with open('./token.txt') as f:
        token = f.read().strip()

    updater = Updater(token=token)
    dispatcher = updater.dispatcher


    dispatcher.add_handler(CommandHandler('start', actions.start))
    dispatcher.add_handler(InlineQueryHandler(actions.inline_search))

    updater.start_polling()


if __name__ == "__main__":
    main()
