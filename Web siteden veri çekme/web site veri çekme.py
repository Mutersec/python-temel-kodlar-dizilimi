import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

    def get_page(self, url):
        response = self.session.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.content
        else:
            return None

    def post_data(self, url, data):
        response = self.session.post(url, data=data, headers=self.headers)
        if response.status_code == 200:
            return response.content
        else:
            return None

    def scrape_data(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        # Veri çekme işlemlerini burada gerçekleştirin
        # Örnek olarak başlık etiketlerini ve resim URL'lerini çekelim
        titles = soup.find_all('h1')
        for title in titles:
            print(title.text)

        images = soup.find_all('img')
        for image in images:
            print(image['src'])

    def perform_scraping(self, url):
        html = self.get_page(url)
        if html:
            self.scrape_data(html)
        else:
            print('Sayfa alınamadı.')

# Örnek kullanım
if __name__ == '__main__':
    scraper = WebScraper()
    url = 'https://example.com'  # Scraping yapmak istediğiniz web sayfasının URL'si
    scraper.perform_scraping(url)

#Muter tarafından yazılmıştır.

#Discord:https://discord.gg/WRWEk6jKG7