from telegram import InlineQueryResultArticle, InputTextMessageContent


def cards_to_articles(cards: dict):
    results = []
    for card in cards['data']:
        description = card.get('oracle_text', card.get('type_line', ''))
        thumbnail = card['image_uris']['small'] if 'image_uris' in card else None

        results.append(InlineQueryResultArticle(
            id=card['id'],
            title=card['name'],
            url=card['scryfall_uri'],
            description=description,
            thumb_url=thumbnail,
            hide_url=True,
            input_message_content=InputTextMessageContent(
                message_text=card['scryfall_uri'],
                disable_web_page_preview=False
            )
            ))

    return results
