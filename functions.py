import telebot
import random

bot = telebot.TeleBot('6707418792:AAEs4Ig-li1t3IeIakjgiHJ3V7I905jHtqE')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Спроси как у меня дела")

@bot.message_handler(func=lambda message: message.text.lower() == 'как дела?')
def handle_how_are_you(message):
    responses = ["Хорошо!", "Нормально.", "Не очень."]
    response = random.choice(responses)

    bot.send_message(message.chat.id, response)
