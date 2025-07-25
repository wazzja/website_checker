import time
import random
import datetime
import requests
from fetch import fetch_url
from logger import logger, log_change
from diff import check4changes
from config import URL, BOT_TOKEN, CHAT_ID


def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        resp = requests.post(telegram_url, data=data)
        if not resp.ok:
            print(f"[Error] Telegram API error: {resp.text}")
    except Exception as e:
        print(f"[Error] Failed to send Telegram message: {e}")

def monitor_website(url):
    try:
        print("Starting website monitor...")
        l_c = fetch_url(url)

        if not l_c:
            print("Initial fetch failed, exiting.")
            return
        else:
            logger.info(f"Initial fetch:\n\n{l_c}")

        while True:
            wait_sec = random.randint(30, 90)
            now = datetime.datetime.now()

            print(f"[{now:%Y-%m-%d %H:%M:%S}]\nWaiting {wait_sec} seconds before next check...\n")
            time.sleep(wait_sec)

            c_c = fetch_url(url)
            if not c_c:
                continue

            if l_c != c_c:
                send_telegram_message(f"Website changed:\n{url}")
                print("Change detected!\n")
                log_change(check4changes(l_c, c_c))
                l_c = c_c
            else:
                print("No change detected.\n")
    except KeyboardInterrupt:
        print("\nMonitoring stopped")

if __name__ == "__main__":
    monitor_website(URL)
