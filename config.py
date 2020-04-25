import os

class Config:

    '''
    Class creates Config objects
    '''
    #set environment variables
    BASE_URL = "https://newsapi.org/v2/{}?language=en&apiKey={}"
    NEWS_API_KEY = os.environ['NEWS_API_KEY']
    SECRET_KEY = os.environ['SECRET_KEY']

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

