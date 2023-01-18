from telethon.tl.types import Channel
from tgtg import TgtgClient
from telethon import TelegramClient, events, sync, functions, types
from datetime import datetime, time
from pytz import timezone, utc
import config
import time as tm
import subprocess
import random

def in_between(now, start, end):
    if start <= end:
        return start <= now < end
    else: # over midnight e.g., 23:30-04:15
        return start <= now or now < end
# setup
pacific = timezone('US/Pacific')
first_run = True
exception_count = 0

args = f'{config.vpn["vpn-script-location"]}'

## Begin VPN
subprocess.Popen(args, stdin=None, stdout=None, stderr=None, close_fds=True)
tm.sleep(30)


## Login to TGTG
tgtg_client = TgtgClient(email=config.tgtg['email'], access_token=config.tgtg['access_token'],
                    refresh_token=config.tgtg['refresh_token'],
                    user_id=config.tgtg['user_id'])

## Setup Telegram bot
telegram_client = TelegramClient(config.telegram['bot_id'], config.telegram['api_id'], config.telegram['api_hash'])
telegram_client.start(bot_token=config.telegram["bot_token"])
# telegram_client(functions.account.ResetAuthorizationRequest(hash=-12398745604826))
# telegram_client.log_out()

print(telegram_client.session.list_sessions())

already_notified = {}

while True:
    now = datetime.now(pacific).time()

    if in_between(now,time(8),time(23)) or first_run:

        first_run = False

        try:

            update = tgtg_client.get_items()

            exception_count = 0

            for i in update:
                if int(i['items_available']) == 0 and i['display_name'] in already_notified:
                    del already_notified[i['display_name']]

                # if (i['items_available'] > 0 and i['display_name'] not in already_notified) or (
                #         i['display_name'] in already_notified and int(already_notified[i['display_name']]) != int(i['items_available'])
                #         and int(i['items_available'] > 0)):
                #     already_notified[i['display_name']] = i['items_available']
                #     now = str(datetime.today().strftime("%I:%M %p"))
                #     message = f"**{i['display_name']}** is available! (Items available:**{i['items_available']}**, Time:{now})"
                #     result = telegram_client.send_message(entity=config.telegram['channel_id'], message = message, silent=False)

                if (i['items_available'] > 0 and i['display_name'] not in already_notified):
                    already_notified[i['display_name']] = i['items_available']
                    now = str(datetime.today().strftime("%I:%M %p"))
                    message = f"**{i['display_name']}** is available! (Items available:**{i['items_available']}**, Time:{now})"
                    result = telegram_client.send_message(entity=config.telegram['channel_id'], message = message, silent=False)           
                    
                    print(message)

            random_number = random.randint(0,6)
            tm.sleep(30 + random_number)

        except Exception as e:
            exception_count = exception_count + 1
            if exception_count == 3:
                exit()
            print("Issues with Internet Connection...")
            subprocess.Popen(args , stdin=None, stdout=None, stderr=None, close_fds=True)
            print(e)
            tgtg_client = TgtgClient(email=config.tgtg['email'], access_token=config.tgtg['access_token'],
                        refresh_token=config.tgtg['refresh_token'],
                        user_id=config.tgtg['user_id'])
            telegram_client.start(bot_token=config.telegram["bot_token"])

    

