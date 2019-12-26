from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from env import NEWS_API_KEY, BOT_API_KEY

import datetime

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


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(BOT_API_KEY, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()