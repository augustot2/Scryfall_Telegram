import logging

import requests


log = logging.getLogger(__name__)


BASE_URL = "https://api.scryfall.com/"


def cards_search(query: str, order: str = None, page: int = 1):
    response = requests.get(BASE_URL + 'cards/search',
                            params={
                                'q': query,
                                'order': order or 'name',
                                'page': page
                            })

    if response.status_code >= 400:
        log.error("Scryfall API error: " + scryfall)
        return None

    content = response.json()

    return content

