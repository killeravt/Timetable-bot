import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types
bot = telebot.TeleBot("1467455929:AAFyqb9WXV5s31HRO3s3DQ1ZpLFR2-kg1sM")

@bot.message_handler(commands=['start'])
def start_handler(message):
  bot.send_message(message.chat.id, "Для получения ссылки на скачку расписания пропиши: /link")

@bot.message_handler(commands=['link'])
def link_handler(message):
  URL = 'https://e-u.in.ua/ua/studentu/rozklad-zanjat/'
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.456'}
  full_page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(full_page.content, 'html.parser')
  roz = soup.findAll('a', href=True)[94]
  res = roz
  orig1 = str(res).replace('<a href=".',"https://e-u.in.ua/ua/studentu/rozkrad-zanjat")
  orig2 = str(orig1).replace('" target="_blank">2 курс (ФЕМ, ФІСТ)</a>', '')
  bot.send_message(message.chat.id, orig2)

bot.polling(none_stop = True)
