import datetime

from SingletonByArgs import SingletonByArgs
from factorization import gnu_factor

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext.dispatcher import run_async

MAX_INPUT_SIZE = 1000 # 1Kb of text

def start(update, context):
    update.message.reply_text('Hello, type some numbers to factor them.')

def help(update, context):
    update.message.reply_text('Type numbers to factor them. Any not valid number will be ignored, ex: 123dz')    

def reply(update, context):
    bot = context.bot
    chat_id = update.message.chat_id
    input = update.message.text
    print(input)
    if len(input) > MAX_INPUT_SIZE:
        bot.send_message(chat_id, 'Input size is to big. Please, send message with 1000 or less characters.')
    else:
        try:
            bot.send_message(chat_id, 'Factoring...')
            output = gnu_factor(input)
            bot.send_message(chat_id, output)
        except Exception as e:
            print ("Error: " + str(e))
        

class FactorNumbersBot(metaclass=SingletonByArgs):
    def __init__(self, bot_api_key):
        self.updater = Updater(bot_api_key, use_context=True)
        dp = self.updater.dispatcher

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        dp.add_handler(MessageHandler(Filters.text, reply))

    def start(self):
        print(self.updater)
        return self.updater.start_polling(poll_interval=0.12)

    def stop(self):
        self.updater.stop()


def main():
    pass

if __name__ == '__main__':
    main()
