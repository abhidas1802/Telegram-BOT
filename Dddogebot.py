import logging
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import Update,Bot

logging.basicConfig(format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',level=logging.INFO)
logger=logging.getLogger(__name__)

TOKEN="xxxxxx"

def start(bot,update):
    print(update)
    author=update.message.from_user.first_name
    reply="Hi! {}".format(author)
    bot.send_message(chat_id=update.message.chat_id,text=reply)

def help(bot,update):
    help_txt="Hey! Here's the list of all the commands."
    bot.send_message(chat_id=update.message.chat_id,text=help_txt)

def echo_text(bot,update):
    reply=update.message.text
    bot.send_message(chat_id=update.messsage.chat_id,text=reply)

def echo_sticker(bot,update):
    bot.send_sticker(chat_id=update.message.chat_id,sticker=update.message.sticker.file_id)

def error(bot,update):
    logger.error("Update '%s' caused error '%s'",update,update.error)




def main():
    updater=Updater(TOKEN)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help))
    dp.add_handler(MessageHandler(Filters.text,echo_text))
    dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
    dp.add_error_handler(error)

    updater.start_polling()
    logger.info("Polling has started...")
    updater.idle()

if __name__=="__main__":
    main()
