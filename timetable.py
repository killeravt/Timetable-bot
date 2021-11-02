import telebot
import schedule
import sched, time
import threading
import requests
from bs4 import BeautifulSoup
from telebot import types
from multiprocessing.context import Process
bot = telebot.TeleBot("1661490916:AAFkeqWMCVbSqk722ERR7ljzbrgQzl_4ecg")
#bot = telebot.TeleBot("1407745525:AAFtQlzk9A99dKX0naKXPNynUAXozY2CrW0")
@bot.message_handler(commands=['start'])
def start_handler(message):
  bot.send_message(message.chat.id, "Для получения ссылки на скачку расписания пропиши: /link. \nДля отображения информации для входа конференций Zoom пропиши: /info")

@bot.message_handler(commands=['help'])
def help_handler(message):
  bot.send_message(message.chat.id,"/link - для получения информации, /info - пароли для зума")

#группа -1001364384740
# колиж -403477493
#тест -599081025

@bot.message_handler(commands=['link'])
def link_handler(message):
  URL = 'https://e-u.in.ua/ua/studentu/rozklad-zanjat/'
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.186'}
  full_page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(full_page.content, 'html.parser')
  c = 103
  roz = soup.findAll('a', href=True)[c]
  res = roz
  print(roz)
  if "3 курс (ФЕМ, ФІСТ)" in res:
    cont = "yes"
  else:
    cont = "no"
  if cont == "yes":
    orig1 = str(res).replace('<a href=".',"https://e-u.in.ua/ua/studentu/rozkrad-zanjat")
    orig2 = str(orig1).replace('" target="_blank">3 курс (ФЕМ, ФІСТ)</a>', '')
    bot.send_message(message.chat.id, orig2)
  if cont == "no":
    if "4 курс (ФЕМ, ФІСТ)" in res:
      URL = 'https://e-u.in.ua/ua/studentu/rozklad-zanjat/'
      headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.456'}
      full_page = requests.get(URL, headers=headers)
      soup = BeautifulSoup(full_page.content, 'html.parser')
      roz = soup.findAll('a', href=True)[c-1]
      res = roz
      orig1 = str(res).replace('<a href=".',"https://e-u.in.ua/ua/studentu/rozkrad-zanjat")
      orig2 = str(orig1).replace('" target="_blank">3 курс (ФЕМ, ФІСТ)</a>', '')
      bot.send_message(message.chat.id, orig2)
    if "1 курс (всі спеціальності)" in res:
      URL = 'https://e-u.in.ua/ua/studentu/rozklad-zanjat/'
      headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.456'}
      full_page = requests.get(URL, headers=headers)
      soup = BeautifulSoup(full_page.content, 'html.parser')
      roz = soup.findAll('a', href=True)[c+2]
      res = roz
      orig1 = str(res).replace('<a href=".',"https://e-u.in.ua/ua/studentu/rozkrad-zanjat")
      orig2 = str(orig1).replace('" target="_blank">3 курс (ФЕМ, ФІСТ)</a>', '')
      bot.send_message(message.chat.id, orig2)
    if "2 курс (ФЕМ, ФІСТ)" in res:
      URL = 'https://e-u.in.ua/ua/studentu/rozklad-zanjat/'
      headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.456'}
      full_page = requests.get(URL, headers=headers)
      soup = BeautifulSoup(full_page.content, 'html.parser')
      roz = soup.findAll('a', href=True)[c+1]
      res = roz
      orig1 = str(res).replace('<a href=".',"https://e-u.in.ua/ua/studentu/rozkrad-zanjat")
      orig2 = str(orig1).replace('" target="_blank">3 курс (ФЕМ, ФІСТ)</a>', '')
      bot.send_message(message.chat.id, orig2)


@bot.message_handler(commands=['system'])
def ukr_handler(message):
  bot.send_message(message.chat.id, "Котетунов В.Ю")
  bot.send_message(message.chat.id, "75816370994")
  bot.send_message(message.chat.id, "is7v4f")
  bot.send_message(message.chat.id, "https://www.google.com/url?q=https://us04web.zoom.us/j/6878969975?pwd%3DTzRpT05zaXkxMW04eUEzdWxMYzNJZz10&sa=D&source=editors&ust=1635835920524000&usg=AOvVaw0SbNBNyHtwFKPKp1tJUIWp")


@bot.message_handler(commands=['angl'])
def ukr_handler(message):
  bot.send_message(message.chat.id, "Гараган К.О")
  bot.send_message(message.chat.id, "3435773605")
  bot.send_message(message.chat.id, "430668")
  bot.send_message(message.chat.id, "https://www.google.com/url?q=https://us04web.zoom.us/j/3435773605?pwd%3DZzY0a1ZVc1BOS1VIQTJmTEVuK0NCZz09&sa=D&source=editors&ust=1634554573979000&usg=AOvVaw2STuK7c37yGpyXYdt98W_f")

@bot.message_handler(commands=['prog'])
def ukr_handler(message):
  bot.send_message(message.chat.id, "Тригубенко І. Б")
  bot.send_message(message.chat.id, "84098239232")
  bot.send_message(message.chat.id, "111111")
  bot.send_message(message.chat.id, "https://www.google.com/url?q=https://us05web.zoom.us/j/84098239232?pwd%3Dd0haa1NwYlRybmZwZ05qNlB1dm4zQT09&sa=D&source=editors&ust=1634554573985000&usg=AOvVaw2VLD8UGixvUyRgO2tNrI6h")
  
@bot.message_handler(commands=['mereji'])
def ukr_handler(message):
  bot.send_message(message.chat.id, "Левченко С. В")
  bot.send_message(message.chat.id, "https://us04web.zoom.us/j/6878969975?pwd=TzRpT05zaXkxMW04eUEzdWxMYzNJZz09")


@bot.message_handler(commands=['info'])
def info_handler(message):
  bot.send_message(message.chat.id, "Команды для зума: Комп. системи - /system \n Англ мова - /angl \n Програмування - /prog \n Орг. комп. мереж - /mereji")


bot.polling(none_stop=True)

