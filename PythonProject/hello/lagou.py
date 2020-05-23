

#抓取拉勾网站中“产品总监”岗位的信息

from bs4 import BeautifulSoup
import requests
import csv
import time
import random
import codecs

# url = 'https://www.lagou.com/jobs/list_%E4%BA%A7%E5%93%81%E6%80%BB%E7%9B%91/p-city_3?&cl=false&fromSearch=true&labelWords=&suginput='

url = 'https://www.lagou.com/jobs/7153122.html?source=pl&i=pl-6&show=5a461494803d46c09eb4f57775bc227f'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text,'html.parser')

i = 1
rows = []
rows.append(['Company','Position','Salary','Responsibility','Requirement',])

company = soup.find('h4',class_='company').get_text()
position = soup.find('h1',class_='name').get_text()
salary = soup.find('span',class_='salary').get_text()

job_detail = soup.find('div',class_='job-detail').get_text().strip()
head, sep, tail = job_detail.partition('任职要求')

responsibility = head.replace('职位描述','')
requirement = tail


rows.append([company,position,salary,responsibility,requirement])

print(company,position,salary,responsibility)


with open('job.csv', 'w', encoding='utf-8-sig',newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows) 