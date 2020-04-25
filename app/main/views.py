from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_headlines

@main.route('/')
def index():

    '''
    View function, which returns the index page and its contents
    '''
    news_sources = get_sources('sources')
    top_headlines = get_headlines('top-headlines')
    title = 'News-Flash'
    return render_template('index.html',title=title,sources=news_sources,headlines=top_headlines)