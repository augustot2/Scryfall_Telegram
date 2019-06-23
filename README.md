# scryfall_telegram #

*Note: This project still works, but @ScryfallBot is now powered by this spiritual successor: [scryfall-telegram-rs-serverless](https://github.com/OliverHofkens/scryfall-telegram-rs-serverless)*

Scryfall Telegram is an inline [Telegram](https://telegram.org/) bot that uses
[Scryfall](https://scryfall.com/)'s API to search Magic: The Gathering cards.

All Scryfall syntax that can be understood by the API can be used. A full reference
can be found here: [Scryfall Syntax Reference](https://scryfall.com/docs/reference).

Some examples:
- Search a card by name: `@ScryfallBot Bolas`
- Search an instant that can be played in an Esper EDH deck: `@ScryfallBot id<=esper t:instant`
- Search cards that enter the battlefield tapped: `@ScryfallBot o:"~ enters the battlefield tapped"`

## Running it yourself

This bot lives on Telegram: [t.me/ScryfallBot](t.me/ScryfallBot),
but you can easily run a copy of it yourself:

### Requirements
- Python 3.6

### Installation
- Clone this repository
- In the root of the project, run `pip install .`
- Add a file called `token.txt` to the root of the project, containing your
Telegram bot API token ([The Botfather](https://core.telegram.org/bots#6-botfather) will help you with that)
- Run it with `scryfall-telegram`
