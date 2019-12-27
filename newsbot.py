import datetime

from SingletonByArgs import SingletonByArgs

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from env import NEWS_API_KEY
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key=NEWS_API_KEY)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello type some keywords to start searching for news on the web.')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Hello type some keywords to start searching for news on the web.')    

def echo(update, context):
    print (update)
    """Echo the user message."""
    today = datetime.datetime.utcnow()
    last_week = today - datetime.timedelta(weeks=3)
    all_articles = newsapi.get_everything(q=update.message.text,
                                      sources='bbc-news,the-verge,abc-news-au,bbc-sport,bloomberg,crypto-coins-news,engadget,espn,national-geographic',
                                      from_param=today,
                                      to=last_week,
                                      language='en',
                                      sort_by='relevancy')
    for i in all_articles['articles'][:3]:
        update.message.reply_text("%s\n\n%s" % (i['source']['name'], i['url']))
    
    if len(all_articles['articles']) == 0:
        update.message.reply_text("No related news has been found. Try to simplify what you want with keywords.")


class NewsBot(metaclass=SingletonByArgs):
    def __init__(self, news_bot_api_key):
        self.updater = Updater(news_bot_api_key, use_context=True)
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