from flask import Blueprint

#initialize blueprint class
main = Blueprint('main',__name__)
from . import views,error