from setuptools import setup

from scryfall_telegram import __prog__, __version__


setup(
    name='scryfall-telegram',
    version=__version__,
    description='Telegram bot to interact with the Scryfall API',
    author='Oliver Hofkens',
    author_email='oliver.hofkens@tuta.io',
    url='https://github.com/OliverHofkens/Scryfall_Telegram',
    packages=['scryfall_telegram'],
    keywords="telegram scryfall mtg tcg bot",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: No Input/Output (Daemon)",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Communications :: Chat",
        "Topic :: Games/Entertainment"
    ],
    entry_points={
        'console_scripts': [
            '%s=scryfall_telegram.main:main' % __prog__,
        ]
    },
    install_requires=[i.strip() for i in open("requirements.txt").readlines()]
)
