from flask import render_template,request,redirect,url_for

from . import main
from ..requests import get_sources,get_headlines,get_source_articles,get_topics

@main.route('/')
def index():

    '''
    View function returns the index page and its contents
    '''
    news_sources = get_sources('sources')
    top_headlines = get_headlines('top-headlines')
    title = 'News-Flash'
    return render_template('index.html',title = title,sources = news_sources,headlines = top_headlines)
    

@main.route('/about')
def about():

    '''
    View function returns about us page and its contents
    '''
    title = "About News-Flash"
    return render_template('about.html',title = title)

@main.route('/source/<id>')
def source(id):

    '''
    View function returns source details page
    '''
    id = get_source_articles(id)
    

    return render_template('source.html',id = id)

@main.route('/coronavirus')
def coronavirus():

    '''
    View function returns view that has articles on coronavirus
    '''
    coronavirus_list = get_topics('coronavirus')
    return render_template('coronavirus.html',coronavirus = coronavirus_list)
    