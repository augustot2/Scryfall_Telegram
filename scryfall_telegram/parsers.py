from telegram import InlineQueryResultArticle, InputTextMessageContent


def cards_to_articles(cards: dict):
    return [InlineQueryResultArticle(
            id=card['id'],
            title=card['name'],
            url=card['scryfall_uri'],
            description=card['oracle_text'],
            thumb_url=card['image_uris']['small'],
            hide_url=True,
            input_message_content=InputTextMessageContent(
                message_text=card['scryfall_uri'],
                disable_web_page_preview=False
            )
            ) for card in cards['data']]
