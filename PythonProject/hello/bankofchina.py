from bs4 import BeautifulSoup
import requests
import csv


def download_page(url):
    # 模拟网页头内容
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)
    # 返回html内容
    return r.text

def get_content(html):

    # 用 Beautiful Soup 解析 html 数据，并保存在 soup 变量里
    soup = BeautifulSoup(html, 'html.parser')

    # 在表格中查找数据
    table = soup.find('table')
    results = table.find_all('tr')

    # 创建一个列表对象，并且把表头数据作为列表的第一个元素
    rows = []
    rows.append(['Public Date', 'Period',
                'LPR(%)'])

    # 遍历所有数据
    for result in results:
        # 找到每一个 td 单元格的内容
        data = result.find_all('td')
        # 如果该单元格无数据，则跳过
        if len(data) == 0: 
            continue
        # 将单元格内容保存到变量中
        public_date = data[0].getText()
        period = data[1].getText()
        lpr = data[2].getText()   
        
        # 将信息添加到 rows 对象里
        rows.append([public_date, period,lpr])
    # 将rows对象写入文件中
    save_info(rows)


def save_info(*args):
    for i in args:
        with open('interesthistory.csv', 'w', encoding='utf-8',newline='') as f_output:
            csv_output = csv.writer(f_output)
            csv_output.writerows(i)


def main():
    # 把网址 URL 存在变量里
    urlpage =  'https://www.bankofchina.com/fimarkets/lilv/fd32/201310/t20131028_2578984.html'
    html = download_page(urlpage)
    get_content(html)

if __name__ == '__main__':
    main()