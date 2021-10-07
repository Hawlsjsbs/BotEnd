import telebot
token = "2065968320:AAHuVBolVHIoDE2bAmjVg_Ssjfa-CQgIqY8"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(message):
	startmessage="""
👋 Welcome @%s in Bot ID 👋
🔱 To Know ID Send 🔱
👁‍🗨 ==> /id_info
	"""%message.chat.username
	bot.send_message(message.chat.id, text=startmessage)
@bot.message_handler(commands=["id_info"])
def id_info(message):
	idmessage="""
♥ Welcom Back @%s
📣 Your ID ==> %s

🔐 Owner ==> @Z_9_U
🔐 Channel ==> @Qa_GaMe
	"""%(message.chat.username, int(message.chat.id))
	bot.send_message(message.chat.id, text=idmessage)
	if str(message.chat.id) != str("1875412243"):
		order = """
✍ < New Order > ✍
📤 User Name ==> @%s
📤 ID ==> %s	
	"""%(message.chat.username, message.chat.id)
		bot.send_message("1875412243", text=order)
	



bot.polling(True)
