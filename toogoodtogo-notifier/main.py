from tgtg import TgtgClient
from telethon import TelegramClient, events, sync
from datetime import datetime
import config
import time as tm

# setup

tgtg_client = TgtgClient(email=config.tgtg['email'], access_token=config.tgtg['access_token'],
                    refresh_token=config.tgtg['refresh_token'],
                    user_id=config.tgtg['user_id'])

telegram_client = TelegramClient('TooGoodToGO Notifier', config.telegram['api_id'], config.telegram['api_hash'])
telegram_client.start()

already_notified = {}

while True:

    update = tgtg_client.get_items()

    for i in update:
        if int(i['items_available']) == 0 and i['display_name'] in already_notified:
            del already_notified[i['display_name']]

        if (i['items_available'] > 0 and i['display_name'] not in already_notified) or (
                i['display_name'] in already_notified and int(already_notified[i['display_name']]) != int(i['items_available'])
                and int(i['items_available'] > 0)):
            already_notified[i['display_name']] = i['items_available']
            now = str(datetime.today().strftime("%I:%M %p"))
            message = f"{i['display_name']} is available! (Items available:{i['items_available']}, Time:{now})"
            telegram_client.send_message('adamnguyen1992', message)
            print(message)

    tm.sleep(5)


    

