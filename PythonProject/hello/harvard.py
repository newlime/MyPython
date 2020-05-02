from bs4 import BeautifulSoup
import requests
import csv
import time
import random



def download_page(url):
    # 模拟网页头内容
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)
    # 返回html内容
    return r.text

def get_content(html):

    i = 1
    # 用 Beautiful Soup 解析 html 数据，并保存在 soup 变量里
    soup = BeautifulSoup(html, 'html.parser')
    professorlist = soup.find_all('div',class_='faculty-item')

    # 创建一个列表对象，并且把表头数据作为列表的第一个元素
    rows = []
    rows.append(['name', 'title',
                'link'])

    i = 1
    for professor in professorlist:
        time.sleep(random.uniform(1,5))
        name = professor.find('a').text.strip()
        name = name.replace('\n', '').replace('\r', '').replace('\t', '')
        title = professor.find('div',class_='title').text
        link = 'https://www.hbs.edu' + professor.find('a')['href'].strip()
        rows.append([name,title,link])
        
        i = i+1
        if i > 3:
            break
    save_info(rows)


def save_info(*args):
    for i in args:
        with open('harvardprofessor.csv', 'w', encoding='utf-8',newline='') as f_output:
            csv_output = csv.writer(f_output)
            csv_output.writerows(i)


def main():
    # 把网址 URL 存在变量里
    urlpage =  'https://www.hbs.edu/faculty/Pages/browse.aspx'
    html = download_page(urlpage)
    get_content(html)

if __name__ == '__main__':
    main()