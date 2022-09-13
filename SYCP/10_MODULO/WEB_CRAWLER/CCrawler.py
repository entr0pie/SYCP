from bs4 import BeautifulSoup
import requests

class Chicken:
    def get_page(url):
        response = requests.get(url)
        return response
    
    def find_links(html):
        soup = BeautifulSoup(html, 'html.parser')
        hyperlinks = soup.find_all('a')
        
        links = []
        for a in hyperlinks:
            links.append(a['href'])

        return links
    
