import telegram
import sys
import os
TOKEN = os.environ[‘992176702:AAE62G_ubiBo1tGq8x0sQ2W2yYVtfRHBHxk’]
CHAT_ID = -1001168759783
def send_message(event, context):
    bot = telegram.Bot(token=TOKEN)
    bot.sendMessage(chat_id = CHAT_ID, text = "Hey there! Mirage's Bot here")
