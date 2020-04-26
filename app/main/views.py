from flask import render_template,request,redirect,url_for,session
from markupsafe import escape
from . import main
from ..requests import get_sources,get_headlines,get_source_articles

@main.route('/')
def index():

    '''
    View function returns the index page and its contents
    '''
    news_sources = get_sources('sources')
    top_headlines = get_headlines('top-headlines')
    title = 'News-Flash'
    return render_template('index.html',title = title,sources = news_sources,headlines = top_headlines)
    
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    else:
        return 'You are not logged in'

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@main.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

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