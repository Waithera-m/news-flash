from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

boostrap = Bootstrap()

def create_app(config_name):

    '''
    Function initializes app, application configurations, and flask extensions
    '''

    #initialize application
    app = Flask(__name__)

    #initialize configurations
    app.config.from_object(config_options[config_name])

    #initialize flask extensions
    boostrap.init_app(app)

    #register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app