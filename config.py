import os


class Config:

    '''
    Class creates Config objects
    '''
    #set environment variables
    BASE_URL = "https://newsapi.org/v2/{}?language=en&apiKey={}"
    ARTICLES_URL = "http://newsapi.org/v2/top-headlines?sources={}&apiKey={}"
    TOPICS_URL = "https://newsapi.org/v2/everything?q={}&from=2020-04-25&sortBy=popularity&apiKey={}"
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

class ProdConfig(Config):

    '''
    Function inherits general configurations from Config class
    '''
    pass

class DevConfig(Config):

    '''
    Function inherits general configurations from Config class
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}

