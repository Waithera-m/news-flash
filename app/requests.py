from app import create_app
import urllib.request,json
from .models import Item,Source,Article
from functools import reduce

#get api key and base url and set value to none
apiKey = None
base_url = None
articles_url = None

#change the values of api_key and base_url variables
def configure_request(app):

    '''
    Function assigns the values defined in app configuration objects to the api_key and base_url variables
    '''
    global apiKey,base_url,articles_url

    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['BASE_URL']
    articles_url = app.config['ARTICLES_URL']
    #print(articles_url)
    
    

def get_sources(category):

    '''
    Function gets different news sources
    '''
    sources_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']  
            sources_results = modify_results(sources_results_list)

    return sources_results

#transform received results into list
def modify_results(sources_list):

    '''
    Function processes the received data and transforms it into a list

    Args:
        sources_list: List of dictionaries that contain news sources' details
    
    Returns:
        sources_results: a list of news sources objects
    '''

    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')

        if id:
            source_object = Source(id,name,description,url)
            sources_results.append(source_object)
                  
    return sources_results
def get_source_articles(id):

    '''
    Article gets and returns a given source's articles
    '''
              
    #http://newsapi.org/v2/top-headlines?sources={}&apiKey={}
    # id = "abc-news"
    get_articles_url = articles_url.format(id,apiKey)
    # print(get_articles_url)
    # print('hello')
    

    with urllib.request.urlopen(get_articles_url) as url:
        article_details_data = url.read()
        articles_response = json.loads(article_details_data)

        articles_results = None
        if articles_response['articles']:
            articles_results_list = articles_response['articles']
            articles_results = transform_articles(articles_results_list)

    return articles_results

def transform_articles(articles_list):
    
    '''
    Function transforsm received data into a list

    Args:
        articles_list: a list of of dictionaries
    
    Returns:
        articles_results: a list of article objects
    '''
    articles_results = []

    for article_item in articles_list:
        def deep_get(dictionary, keys, default=None):
            
            '''
            Function gets value from nested dictionary
            '''            
            return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)
        id = deep_get(article_item, "source.id")
        author = article_item['author']
        title = article_item['title']
        publishedAt = article_item['publishedAt']
        description = article_item['content']
        url = article_item['url']
        image = article_item['urlToImage']

        if title:
            article_object = Article(id,author,title,publishedAt,description,url,image)
            articles_results.append(article_object)

    return articles_results

        


def get_headlines(category):

    '''
    Function gets top headlines from multiple sources
    '''
    headlines_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        headlines_results = None

        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']  
            headlines_results = process_results(headlines_results_list)

    return headlines_results

def process_results(headlines_list):

    '''
    Function converts received data into a list

    Args:
        headlines_list: list of dictionaries that contain articles' details
    
    Returns:
        headlines_results: a list of article objects
    '''

    headlines_results = []

    for headline_item in headlines_list:
        author = headline_item.get('author')
        title = headline_item.get('title')
        publishedAt = headline_item.get('publishedAt')
        description = headline_item.get('description')
        url = headline_item.get('url')

        if title:
            headline_object = Item(author,title,publishedAt,description,url)
            headlines_results.append(headline_object)

    return headlines_results

    
