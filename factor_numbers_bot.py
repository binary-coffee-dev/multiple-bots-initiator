import datetime

from SingletonByArgs import SingletonByArgs

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    update.message.reply_text('Hello, type some numbers to factor them.')

def help(update, context):
    update.message.reply_text('Type numbers to factor them. Any non valid number will be ignore, ex: 123dz')    

def factor(number):
    primes = []
    prime = 2
    while prime * prime <= number:
        while number % prime == 0:
            primes.append(prime)
            number //= prime
        prime += 1
    if number > 1:
        primes.append(number)
    return primes

def echo(update, context):
    print (update)
    # TODO: get a list of valid numbers from update.message.text
    number = int(update.message.text)
    update.message.reply_text(factor(number))


class FactorNumbersBot(metaclass=SingletonByArgs):
    def __init__(self, bot_api_key):
        self.updater = Updater(bot_api_key, use_context=True)
        # Get the dispatcher to register handlers
        dp = self.updater.dispatcher

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))

    def start(self):
        print(self.updater)
        # Start the Bot
        return self.updater.start_polling(poll_interval=0.12)

    def stop(self):
        self.updater.stop()


def main():
    pass

if __name__ == '__main__':
    main()