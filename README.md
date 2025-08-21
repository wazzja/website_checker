# Intro
A small script that automatically checks for changes in a website's content and sends a message via Telegram when a change is detected.

The script relies primarily on Python 3 standard libraries, with the exception of:

- [`requests`](https://pypi.org/project/requests/) – for sending Telegram messages
- [`selenium`](https://pypi.org/project/selenium/) – for handling dynamically generated HTML using ChromeDriver  
---

## Setup

Tested on Windows with WSL2 in a Python virtual environment.

### 1. Install dependencies

```bash
pip install requests
pip install selenium
```

---

## Config.py

You'll need to write your own config.py file with your personal info in it.
That includes the BOT_TOKEN, your own telegram CHAT_ID, an URL, the SELECTOR and SELECTOR_TYPE you want to watch.

### BOT_TOKEN

Create a bot with [@BotFather](https://t.me/botfather) on Telegram to get your `BOT_TOKEN`.

### CHAT_ID

Send a message to your bot, then visit:

```
https://api.telegram.org/bot<BOT_TOKEN>/getUpdates
```

Look for `"id"` in the JSON response to get your `CHAT_ID`.
### URL
The web address to the particular page you want to be checked

### SELECTOR & SELECTOR_TYPE
The name of the specific HTML widget or class you're monitoring. Currently only works for TAGS and CLASS Typs.

In the end your config.py should look something like this:
```python
URL = "https://website.com"
BOT_TOKEN = "5989402384:ASAJNdhDAKJn8Hnd898hHBDHdhdhd2ayoIH"
CHAT_ID = "3914809149"
SELECTOR = "some-widget"
SELECTOR_TYPE = "CLASS"
```

## Run it

```bash
python monitoring.py
```

## Logging

The initial fetch and all detected changes will be logged. This can help identify which parts of the HTML are necessary to monitor.
