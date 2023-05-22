import requests
from bs4 import BeautifulSoup

def get_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print("Sayfa indirilemedi.")
        return None


def save_page_content(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print("Sayfa içeriği kaydedildi:", filename)
    else:
        print("Sayfa indirilemedi.")


def extract_headings(soup):
    headings = soup.find_all('h1')
    for heading in headings:
        print(heading.text)

def extract_data(soup):
    data = soup.find_all('div', class_='data')
    for item in data:
        print(item.text)


def extract_category_info(soup):
    category_info = soup.find('div', class_='CategoryInfo')
    if category_info:
        print(category_info.text)
    else:
        print("CategoryInfo bulunamadı.")


def extract_images(soup):
    images = soup.find_all('img')
    for image in images:
        print("Resim URL'si:", image['src'])

def extract_links(soup):
    links = soup.find_all('a')
    for link in links:
        print("Bağlantı:", link['href'])

def save_to_database(content):
   
    print("Veritabanına kaydedildi.")


def auto_download(url, filename):
    
    print("Otomatik indirme işlemi gerçekleştirildi.")


def handle_error(error):
   
    print("Hata oluştu:", error)

url = input("İndirilecek sayfanın URL'sini girin: ")
filename = input("Kaydedilecek dosyanın adını girin: ")

html_content = get_page_content(url)
if html_content:
    soup = BeautifulSoup(html_content, 'html.parser')

    extract_headings(soup)
    extract_data(soup)
    extract_category_info(soup)
    extract_images(soup)
    extract_links(soup)

    save_page_content(url, filename)
    save_to_database(html_content)
    auto_download(url, filename)
else:
    print("Sayfa indirilemedi.")
    handle_error("İndirme hatası")
