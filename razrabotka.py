#5155174558:AAGX_E8POu_x17gxwK1ZX1i-LacFL2gYPgw @Tehnologubot
#5249090388:AAGkIzLVsF-TU0Bq7akNaamVwbonkzWdoYI @In_fabot
#Нажми: \nФакт для получения интересного факта\nHit: \nFact to get an interesting fact
#C:\\Users\\User\\Desktop\\Alesha\\facts(en).txt
import sqlite3
import telebot
import random
from telebot import types
from sqlite3 import SQLITE_ALTER_TABLE, Error
f = open('C:\\Users\\User\\Desktop\\Alesha\\факт(ru).txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
f = open('C:\\Users\\User\\Desktop\\Alesha\\fact(en).txt', 'r', encoding='UTF-8')
thinks  = f.read().split('\n')
f.close()
bot = telebot.TeleBot('5249090388:AAGkIzLVsF-TU0Bq7akNaamVwbonkzWdoYI')

@bot.message_handler(commands=['start'])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Факт 🇷🇺")
        item2=types.KeyboardButton('Fact 🇺🇸')
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Нажми: \nФакт для получения интересного факта\nHit: \nFact to get an interesting fact',  reply_markup=markup)
        bot.send_message(m.chat.id, 'Задонать разработчику на QIWI +7 747 455-89-05 ведь он старается :)\nTo give the developer a hard time on QIWI +7 747 455-89-05 because he is trying :)', reply_markup=markup)

        @bot.message_handler(content_types=["text"])
        def handle_text(message, res=False):
                if message.text.strip() == 'Факт 🇷🇺' :
                        answer = random.choice(facts)
                elif message.text.strip() == 'Fact 🇺🇸' :
                        answer = random.choice(thinks)
                bot.send_message(message.chat.id, answer)






bot.polling(none_stop=True, timeout=123)