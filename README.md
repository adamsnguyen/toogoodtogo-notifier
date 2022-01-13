# toogoodtogo-telegram-notifier-bot

This uses the Telegram messaging app to send notifications of your favourite stores when items become available. It will notify you when item availability changes.

You will need to visit here: https://core.telegram.org/ to get access to the Telegram API. There you can register for a bot. 

This python script uses the unofficial TooGoodToGo API client here: https://github.com/ahivert/tgtg-python

## Detailed Steps

1) Run the setup.py file. This will prompt you to login to your TooGoodToGo account. Copy over the credentials to the config.py file.
2) Go to https://core.telegram.org/ to request access to their API and make a new bot through @BotFather. Copy credentials to config.py file.
3) Install the telethon python package

```shell
pip install telethon
```
4) If you haven't done so already, rename the example_config.py to config.py - This is where you're storing your credentials.
5) Run the app. It may require you to login with credentials you already have in the terminal/console. Go to the folder containing main.py and use the command:

```shell
python main.py
```

Enjoy!

## Dependencies

Telethon python package
 
