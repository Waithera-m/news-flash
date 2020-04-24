import  urllib.request,json
from .models import Item,Source

#get api key and base url and set value to none
api_key = None
base_url = None

#change the values of api_key and base_url variables
def configure_request(app):

    '''
    Function assigns the values defined in app configuration objects to the api_key and base_url variables
    '''
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['BASE_URL']

def get_sources(source):
    #change this to get articles function

    '''
    Function gets different news sources
    '''
    get_sources_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.load(get_sources_data)

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']  
            sources_results = modify_results(sources_results_list)

    return sources_results

#transform received results into list
def modify_results(sources_list):

    '''
    Function processes the received data and transforms it into a list

    Args:
        movie_list: List of dictionaries that contain news sources' details
    
    Returns:
        source_results: a list of news sources objects
    '''

    source_results = []
    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')

        if id:
            source_object = Source(id,name,description,url)
            source_results.append(source_object)
                  
    return source_results
