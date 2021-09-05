import requests
from datetime import datetime
from bs4 import BeautifulSoup, SoupStrainer

class Parser:
    def __init__(self, url):
        self.url = url
        

    def get_output(self):
        response = requests.get(self.url)
        response_url = response.url
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title').get_text()
        timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        bodyContent = soup.find(id='bodyContent')
        links = []
        for link in bodyContent.find_all('a'):
            if link.has_attr('href'):
                links.append(link['href'])
        return [title, response_url, len(links), timestamp, links]