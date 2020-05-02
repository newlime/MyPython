from bs4 import BeautifulSoup
import requests
import csv
import time
import random


url = 'https://www.hbs.edu/faculty/Pages/browse.aspx'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text,'html.parser')
professorlist = soup.find_all('div',class_='faculty-item')

i = 1
rows = []
rows.append(['name','title','link'])

for professor in professorlist:
    time.sleep(random.uniform(1,5))
    name = professor.find('a').text.strip()
    name = name.replace('\n', '').replace('\r', '').replace('\t', '')
    title = professor.find('div',class_='title').text
    link = 'https://www.hbs.edu' + professor.find('a')['href'].strip()
    rows.append([name,title,link])
    print(name,title,link)
    
    i = i+1
    if i > 3:
        break

with open('harvardprofessor.csv', 'w', encoding='utf-8',newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows) 