###----------------------------------------------------
#-Owner: Alexey Krasichonak
#-Discription: Send an http alarm to telegram bot via API if memory usage is greater than 80%
###----------------------

import time
import psutil
import requests

def send_tg_msg(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Message was sent.")
    else:
        print("Can't send a message:", response.text)

def check_memory():
    while True:

        memory_usage = psutil.virtual_memory().percent

        if memory_usage > 80:
            bot_token = "###YOUR_TG_TOKEN###"
            chat_id = "###YOUR_CHAT_ID###"
            message = "ALARM! Memory usage is more than 80%: {}%".format(memory_usage)
            send_tg_msg(bot_token, chat_id, message)

        time.sleep(60)

if __name__ == "__main__":
    check_memory()