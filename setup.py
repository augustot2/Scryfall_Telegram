from setuptools import setup

from scryfall_telegram import __prog__, __version__


setup(
    name='scryfall-telegram',
    version=__version__,
    description='Telegram bot to interact with the Scryfall API',
    long_description='',
    author='Oliver Hofkens',
    author_email='oliver@novemberfive.co',
    url='',
    packages=['scryfall_telegram'],
    entry_points={
        'console_scripts': [
            '%s=scryfall_telegram.main:main' % __prog__,
        ]
    },
    install_requires=[i.strip() for i in open("requirements.txt").readlines()]
)
