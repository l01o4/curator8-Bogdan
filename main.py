import telebot
bot = telebot.TeleBot('6562420600:AAGE2liC0ZuaQRF13O8GgaRjrDLbnaD_XaA')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, этот бот создан для тренировки программирования')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Напишите в службу поддержки', parse_mode='Markdown')

@bot.message_handler(commands=['language'])
def main(message):
    bot.send_message(message.chat.id, 'Введите язык, на котором собираетесь программировать', parse_mode='Markdown')

bot.infinity_polling()
