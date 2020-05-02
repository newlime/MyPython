import requests
from bs4 import BeautifulSoup
import csv
import time
import random

# urlpage = 'http://www.sim.cas.cn/dwjs2016/gjrc_129560/fyjygjgcs/'
urlpage = 'https://www.google.com/search?newwindow=1&sxsrf=ALeKk03lhkZ9YYQF30vAEL7OodEajbtOxg%3A1587956378560&ei=mkqmXrHaIdHbtAai24PoCw&q=harvard+pfofessor+list&oq=harvard+pfofessor+list&gs_lcp=CgZwc3ktYWIQAzIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDToECAAQRzoECCMQJzoFCAAQgwE6AggAOgQIABBDOgUIABCRAjoHCAAQFBCHAjoECAAQCjoGCAAQFhAeUPOTC1iw1Qtg2tcLaABwBHgBgAGCBIgBtSiSAQs3LjguNi4zLjEuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwixj_O-zofpAhXRLc0KHaLtAL0Q4dUDCAw&uact=5'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
r = requests.get(urlpage,headers)
soup = BeautifulSoup(r.text,'html.parser')
print('r.text')

# while True:     #一直循环，直到访问站点成功
#         try:
#             #以下except都是用来捕获当requests请求出现异常时，
#             # 通过捕获然后等待网络情况的变化，以此来保护程序的不间断运行
#             r = requests.get(urlpage, headers = headers, timeout = 20)    
#             break
#         except requests.exceptions.InvalidURL:
#             print('InvalidURL -- please wait 3 seconds')
#             time.sleep(3) 
        # except requests.exceptions.ProxyError:
        #     print('ProxyError -- please wait 3 seconds')
        #     time.sleep(3) 
        # except requests.exceptions.RetryError:
        #     print('RetryError -- please wait 3 seconds')
        #     time.sleep(3) 
        # except requests.exceptions.SSLError:
        #     print('SSLError -- please wait 3 seconds')
        #     time.sleep(3) 
        # except requests.exceptions.ConnectionError:
        #     print('ConnectionError -- please wait 3 seconds')
        #     time.sleep(3)
        # except:
        #     print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')
        #     time.sleep(3)


soup = BeautifulSoup(r.text,'html.parser')
table = soup.find('table',class_='table-bordered')
results = table.find_all('tr')

rows = []
rows.append(['name','title','email','address','fax','homepage'])

for i in results:
    time.sleep(random.random()*3)
    data = i.find_all('td')
    if len(data) == 0:
        continue
    name = data[0].getText()
    title = data[1].getText()
    email = data[2].getText()
    address = data[3].getText()
    fax = data[4].getText()
    homepage = data[0].find('a').get('href')
    
    rows.append(data,name,title,email,address,fax,homepage)
    

with open('professor.csv','w',encoding='utf-8',new_line='') as f:
    csv_output = csv.writer(f)
    csv_output.writerows(rows)
    

