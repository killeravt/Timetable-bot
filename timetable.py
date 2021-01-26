import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types
bot = telebot.TeleBot("1467455929:AAFyqb9WXV5s31HRO3s3DQ1ZpLFR2-kg1sM")
@bot.message_handler(commands=['start'])
def start_handler(message):
  bot.send_message(message.chat.id, "Для получения ссылки на скачку расписания пропиши: /link. Для отображения информации для входа конференций Zoom пропиши: /info")

@bot.message_handler(commands=['help'])
def help_handler(message):
  bot.send_message(message.chat.id,"/link - для получения информации, /info - пароли для зума")

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

@bot.message_handler(commands=['ukr'])
def ukr_handler(message):
  bot.send_message(message.chat.id, "Бабінчук Олена Петрівна/Укр.мова")
  bot.send_message(message.chat.id, "662771 1742")
  bot.send_message(message.chat.id, "2RHnBx")

@bot.message_handler(commands=['cult'])
def cult_handler(message):
  bot.send_message(message.chat.id, "Баликін І.І./Культорологiя")
  bot.send_message(message.chat.id, "2103939205")
  bot.send_message(message.chat.id, "671677")

@bot.message_handler(commands=['bezk'])
def bezk_handler(message):
  bot.send_message(message.chat.id, "Бескровний Олексій Іванович/Математика за школою")
  bot.send_message(message.chat.id, "73485639721")
  bot.send_message(message.chat.id, "016871")

@bot.message_handler(commands=['kotov'])
def kotov_handler(message):
  bot.send_message(message.chat.id, "Котвицька Н.М./Економiка,Основи екологiї")
  bot.send_message(message.chat.id, "265-730-45-66")
  bot.send_message(message.chat.id, "5Zcve1")

@bot.message_handler(commands=['varenik'])
def varenik_handler(message):
  bot.send_message(message.chat.id, "Індентифікатор Вареника Б.В/Фізкультура")
  bot.send_message(message.chat.id, "7 412 019 970")
  bot.send_message(message.chat.id, "K96XGw")

@bot.message_handler(commands=['voyna'])
def voyna_handler(message):
  bot.send_message(message.chat.id, "Войнаровська Л. І./Філософія")
  bot.send_message(message.chat.id, "98138858472")
  bot.send_message(message.chat.id, "mBC3LE")

@bot.message_handler(commands=['giyasov'])
def giyasov_handler(message):
  bot.send_message(message.chat.id, "Гіясов Гусейн Аббасович/Спеціальність")
  bot.send_message(message.chat.id, "7863304882")
  bot.send_message(message.chat.id, "953197")

@bot.message_handler(commands=['rudn'])
def rudn_handler(message):
  bot.send_message(message.chat.id, "Рудницька Л.В./Історія України")
  bot.send_message(message.chat.id, "93463988582")
  bot.send_message(message.chat.id, "026623")

@bot.message_handler(commands=['milash'])
def milash_handler(message):
  bot.send_message(message.chat.id, "Милашенко Віктор Миколайович/Спеціальність")
  bot.send_message(message.chat.id, "8382329520")
  bot.send_message(message.chat.id, "12345")

@bot.message_handler(commands=['ukrprof'])
def ukrprof_handler(message):
  bot.send_message(message.chat.id, "Кузьманенко А.В./Укр. мова по спеціальності")
  bot.send_message(message.chat.id, "7238654884")
  bot.send_message(message.chat.id, "auWT5K")

@bot.message_handler(commands=['fortuna'])
def fortuna_handler(message):
  bot.send_message(message.chat.id, "Фортуна Василь Васильович/Висша математика")
  bot.send_message(message.chat.id, "4684579044")
  bot.send_message(message.chat.id, "4684579044")

@bot.message_handler(commands=['opolsky'])
def opolsky_handler(message):
  bot.send_message(message.chat.id, "Фортуна Василь Васильович/Висша математика")
  bot.send_message(message.chat.id, "3832414713")
  bot.send_message(message.chat.id, "12345")

@bot.message_handler(commands=['shyr'])
def shyr_handler(message):
  bot.send_message(message.chat.id, "Щур Євгеній Олександрович/Англійська мова")
  bot.send_message(message.chat.id, "3349349410")
  bot.send_message(message.chat.id, "426902")

@bot.message_handler(commands=['info'])
def info_handler(message):
  bot.send_message(message.chat.id, "Команды для зума: \n/ukr - Укр мова\n /cult Культорологiя\n /bezk Шкільна математика\n /kotov Економiка/Основи екологiї\n /varenik Фізкультура\n /voyna Філософія\n /giyasov Програмування\n /milash Програмування\n /rudn Історія України\n /ukrprof Проф. укр. мова\n /fortuna Висша математика\n /opolsky Фізика\n /shyr Англ. мова")

bot.polling(none_stop = True)
