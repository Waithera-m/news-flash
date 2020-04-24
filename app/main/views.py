from flask import render_template,request,redirect,url_for
from . import main

@main.route('/')
def index():

    '''
    View function, which returns the index page and its contents
    '''
    return render_template('index.html')