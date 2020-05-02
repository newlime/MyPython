from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests

def get_links(link_url)
    response  = requests.get(link_url)
    soup = BeautifulSoup(response.text,'lxml')
    links_div = soup.find_all('div',class_='pic-panel')
    links = [div.a.get('href') for div in links_div]
    return links

def get_page(house_url)
    response  = requests.get(house_url)
    soup = BeautifulSoup(response.text,'lxml')
    return soap

page_url = "https://bj.lianjia.com/zufang/"
house_url = "https://bj.lianjia.com/zufang/BJ2408628366925373440.html"
soup = get_page(house_url)
get_links(url)