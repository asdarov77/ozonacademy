# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uqK12syNR5VNeoTufYIetxznyCjrpP2C
"""

pip install pyTelegramBotApi

import telebot
import random
token='1030911728:AAG9f8OdE8ysuz8iamm8rdbfG62cuos28Es'
bot=telebot.TeleBot(token)
jokes=['Саша,не тупи','Саша ботан','Саша Грей?','Са-са,Ша-ша,Ша-са','Меня зовут Саша, но друзья зовут меня бухать','Саша это как Александр?']

@bot.message_handler(content_types=['text'])
def privet(message):
  if message.text == 'Привет' or 'привет':
      bot.send_message(message.from_user.id, "Как тебя зовут?");
      bot.register_next_step_handler(message, find_alexandr);
def find_alexandr(message):
   if "Саша" in message.text: 
      message.text=random.choice(jokes)
      bot.send_message(message.chat.id, message.text);
      
   else:
      message.text='Жаль что ты не Саша.'
      bot.send_message(message.chat.id, message.text);
   bot.register_next_step_handler(message, repeat_all_mesages);   
def repeat_all_mesages(message):

  if message.text!='хватит':
      mas.append(message.text)
      message.text=random.choice(mas)
      bot.send_message(message.chat.id,message.text);
      bot.register_next_step_handler(message, repeat_all_mesages);
bot.polling()








