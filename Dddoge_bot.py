import logging
from flask import Flask, request
from telegram.ext import Updater, CommandHandler , MessageHandler , Filters, Dispatcher
from telegram import Bot , Update 
#enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s %(message)s', 
	                level= logging.INFO) 
logger = logging.getLogger(__name__)

TOKEN = "xxxxxx"

#webhook-----------------
app = Flask(__name__)

@app.route('/')
def index():
	return "hello!"

@app.route(f'/{TOKEN}' , methods=['GET','POST'])
def webhook():
	'''webhook view which recieves updates from telegram'''
	# create update object from json-format request data
	update = Update.de_json(request.get_json(),bot)
	#process update
	dp.process_update(update)
	return "ok"

#------------------------

def start(bot,update):
	print(update)
	author = update.message.from_user.first_name
	reply = "Hi! {}".format(author)
	bot.send_message(chat_id = update.message.chat_id, text=reply)

def _help(bot,update):
	help_text = "Hey! Here's all the commands"
	bot.send_message(chat_id=update.message.chat_id, text=help_text)

def echo_text(bot,update):
	reply = update.message.text
	bot.send_message(chat_id = update.message.chat_id, text=reply)

def echo_sticker(bot,update):
	bot.send_sticker(chat_id = update.message.chat_id, 
		              sticker= update.message.sticker.file_id)

def error(bot,update):
	logger.error("update '%s' caused error '%s'",update , update.error)
	

##def main():
##	# updater = Updater(TOKEN)       for echo bot
## 	# dp = updater.dispatcher
##	# updater.start_polling()
##	# logger.info("Started polling")       #for echo bot we used polling
##	# updater.idle()

if __name__ == "__main__":
        
        bot = Bot(TOKEN)
        bot.set_webhook("https://1b7e48b7d5f0.ngrok.io/" + TOKEN)

        dp = Dispatcher(bot , None)
        dp.add_handler(CommandHandler("start",start))
        dp.add_handler(CommandHandler("help",_help))
        dp.add_handler(MessageHandler(Filters.text,echo_text))
        dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
        dp.add_error_handler(error)
        app.run(port=8443)
