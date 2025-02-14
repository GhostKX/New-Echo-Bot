import telebot
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = str(os.getenv('API_KEY'))
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start_bot(message):
    user_id = message.from_user.id

    bot.send_message(user_id, f'Hi')
    # bot.send_message(user_id, message)
    bot.register_next_step_handler(message, handling_user_text)


@bot.message_handler(content_types=['text'])
def handling_user_text(message):
    user_id = message.from_user.id
    user_text = message.text
    bot.send_message(user_id, user_text)
    print(message.text)
    bot.register_next_step_handler_by_chat_id(user_id, handling_user_text)


bot.polling(non_stop=True)