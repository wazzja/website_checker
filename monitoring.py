import time
import random
import datetime
from fetcher import get_hash
from logger import log_change
from diff import check_for_changes
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
    print("Starting website monitor...")
    last_hash, last_content = get_hash(url)

    if not last_hash:
        print("Initial fetch failed, exiting.")
        return

    while True:
        wait_seconds = random.randint(30, 90)
        now = datetime.datetime.now()
        print(f"At {now}\nWaiting {wait_seconds} seconds before next check...\n")
        time.sleep(wait_seconds)

        current_hash, current_content = get_hash(url)
        if not current_hash:
            continue

        if current_hash != last_hash:
            send_telegram_message(f"Website changed:\n{url}")
            print("Change detected!\n")
            log_change(check_for_changes(last_content, current_content))
            last_hash = current_hash
            last_content = current_content
        else:
            print("No change detected.\n")

if __name__ == "__main__":
    monitor_website(URL)
