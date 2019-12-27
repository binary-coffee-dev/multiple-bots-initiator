from env import NEWS_BOT_API_KEY

if NEWS_BOT_API_KEY != None:
    from newsbot import NewsBot
    newsBot = NewsBot(NEWS_BOT_API_KEY)
    newsBot.start()

####################################################

from env import FACTOR_NUMBERS_BOT_API_KEY

if FACTOR_NUMBERS_BOT_API_KEY != None:
    from factor_numbers_bot import FactorNumbersBot
    factorBot = FactorNumbersBot(FACTOR_NUMBERS_BOT_API_KEY)
    factorBot.start()

