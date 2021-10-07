import telebot
token = "2065968320:AAHuVBolVHIoDE2bAmjVg_Ssjfa-CQgIqY8"
bot = telebot.TeleBot(token, parse_mode=None)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

bot.polling(True)
