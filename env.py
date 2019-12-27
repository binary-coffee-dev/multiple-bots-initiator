import os

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

if NEWS_API_KEY == None:
    from env_secret import NEWS_API_KEY

NEWS_BOT_API_KEY = os.environ.get('NEWS_BOT_API_KEY')

if NEWS_BOT_API_KEY == None:
    from env_secret import NEWS_BOT_API_KEY
