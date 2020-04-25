from app import create_app
import urllib.request,json
from .models import Item,Source

#get api key and base url and set value to none
apiKey = None
base_url = None

#change the values of api_key and base_url variables
def configure_request(app):

    '''
    Function assigns the values defined in app configuration objects to the api_key and base_url variables
    '''
    global apiKey,base_url

    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['BASE_URL']
    
    
    

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
