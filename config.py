import os

class Config:

    '''
    Class creates Config objects
    '''
    #set environment variables
    BASE_URL = 'http://newsapi.org/v2/{}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):

    '''
    Function inherits general configurations from Config class
    '''
    pass

class DevConfig:

    '''
    Function inherits general configurations from Config class
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}

