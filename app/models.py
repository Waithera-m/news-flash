class Item:

    '''
    Class creates news item objects
    '''
    def __init__(self,urlToImage,author,title,publishedAt,description,url):

        '''
        Method facilitates the definition of objects; properties

        Args:
            author (str): article's author 
            title (str): article's title
            publishedAt (str): article publication date
            description (str): brief description of article content
            urlToImage (str): link to new's item image
            url (str): link to full article
        '''

        self.urlToImage = urlToImage
        self.author = author
        self.title = title
        self.publishedAt = publishedAt
        self.description = description
        self.url = url
        
