import telebot

bot = telebot.TeleBot('5470180373:AAGitG7EN1R6sQyTstg84lkyXnxMC3Y2XQY')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b><u>{message.from_user.first_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    bot.send_message(message.chat.id, message, parse_mode='html')

bot.polling(none_stop=True)