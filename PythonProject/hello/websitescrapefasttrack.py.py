from bs4 import BeautifulSoup
import requests
import csv

# 参考文献：https://oicebot.github.io/2018/09/30/data-science-skills-web-scraping-using-python.html


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
    table = soup.find('table', attrs={'class': 'tableSorter2'})
    results = table.find_all('tr')

    # 创建一个列表对象，并且把表头数据作为列表的第一个元素
    rows = []
    rows.append(['Rank', 'Company Name',
                'Webpage', 'Description',
                'Location', 'Year end',
                'Annual sales rise over 3 years', 'Sales Rise','Latest sales',
                'Staff', 'Comments']
                )

    # 遍历所有数据
    for result in results:
        # 找到每一个 td 单元格的内容
        data = result.find_all('td')
        # 如果该单元格无数据，则跳过
        if len(data) == 0: 
            continue
        # 将单元格内容保存到变量中
        rank = data[0].getText()
        company = data[1].getText()
         # 提取公司链接内容
        webpage = data[1].find('a').get('href')
        # 提取公司名字    
        companyname = data[1].find('span', attrs={'class':'company-name'}).getText()    
        description = company.replace(companyname, '')
        location = data[2].getText()
        yearend = data[3].getText()
        salesrise = data[4].getText()
        sales = data[5].getText()
        # 删除多余的字符
        sales = sales.strip('*').strip('†').replace(',','')
        staff = data[6].getText()
        comments = data[7].getText()	
        
        # 将公司信息添加到 rows 对象里
        rows.append([rank, companyname,
                    webpage, description, 
                    location, yearend, 
                    salesrise, sales, 
                    staff, comments]
                    )
    # 将rows对象写入文件中
    save_info(rows)


def save_info(*args):
    for i in args:
        with open('techtrack100.csv', 'w', encoding='utf-8',newline='') as f_output:
            csv_output = csv.writer(f_output)
            csv_output.writerows(i)


def main():
    # 把网址 URL 存在变量里
    urlpage =  'https://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'
    html = download_page(urlpage)
    get_content(html)

if __name__ == '__main__':
    main()