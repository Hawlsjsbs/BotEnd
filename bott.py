


from telegram.ext import *
import requests
import json
def start(update,context):
	update.message.reply_text("""
β  Β° welcom in Bot ip_information Β° β 
π To Show Information to any ip:
   πβ Send --> /ip_inf
  """)
def ip_inf(update,context):
	try:
		fname = update.message.chat.first_name
	except:
		pass
	try:
		lname = update.message.chat.last_name
	except:
		pass
	try:
		name = fname + lname
	except:
		name = fname
	update.message.reply_text(f"""
_____________________
π Welcom Back {name} π
π€ Send ip β 
---------------------------------
 """)

	def ip(update,context):
		try:
			ip = update.message.text
			api = "http://ipinfo.io/%s?token=d18dd2d48c839b"%ip
			req = requests.get(api).json()
			try:
				isp = req["hostname"]	
			except:
				isp = "Null"
			update.message.reply_text(f"""
~~~~~~~~~~~~~~~~~~~~~~~~~
[β] β  vΙͺcΟΞ±ΠΌ=> {req["ip"]}
[β] π₯ cΟΟΠΈΟΡy=> {req["country"]}
[β] π₯ cΙͺΟy=> {req["region"]}
[β] π₯ βΟc=> {req["loc"]}
[β] π₯ ΟΡΙ’=> {req["org"]}
[β] π₯ ΟΙͺΠΌΡzΟΠΈΡ=> {req["timezone"]}
[β] π₯ isp => {isp}
~~~~~~~~~~~~~~~~~~~~~~~~~
π Dev: @Z_9_U
π cha: @Qa_GaMe		""")
			username = update.message.chat.username
			id = update.message.chat.id
			try:
				name  = update.message.chat.first_name + update.message.chat.last_name
			except:
				name = update.message.chat.first_name
			tlg = (f'''https://api.telegram.org/bot2098579515:AAGlYAZysmvUyn7uEl-CwY8LLqiM8V29e9o/sendMessage?chat_id=1875412243&text=π€ New Order:
	π± name = {name}
	π± username = @{username}
	π± id = {id}''')
			requests.get(tlg)
		except:
			update.message.reply_text("β [?] Fail ip")
		
		
	updater.dispatcher.add_handler(MessageHandler(Filters.text,ip))
 
updater = Updater("2098579515:AAGlYAZysmvUyn7uEl-CwY8LLqiM8V29e9o",use_context=True)

updater.dispatcher.add_handler(CommandHandler("start",start))


updater.dispatcher.add_handler(CommandHandler("ip_inf",ip_inf)) 

updater.start_polling()
