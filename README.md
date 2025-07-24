# Intro
A small script to automate checking if a website changes its content, in which case it sends a message to you on Telegram.
It runs mostly librarys that are included in python3 with the exception of "requests" library

### Config.py
You'll need to write your own conig.py file with your personal info in it.
That includes the BOT_TOKEN, your own telegram CHAT_ID and an URL.

###### BOT_TOKEN
Through the telegrambot 'BotFather' you can easily create your own bot and get access to its BOT_TOKEN.

###### CHAT_ID
Now you'll have to send a message to your own bot and visit this site:
https://api.telegram.org/bot<BOT_TOKEN>/getUpdates
There you can find the CHAT_ID under id:

###### URL
The web address to the particular page you want to be checked

In the end your config.py should look something like this:
  <html>
    <head>
      URL = "https://website.com"
      BOT_TOKEN = "5989402384:ASAJNdhDAKJn8Hnd898hHBDHdhdhd2ayoIH"
      CHAT_ID = "3914809149"
    </head>
  </html>
