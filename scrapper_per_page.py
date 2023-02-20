import requests as rq
from bs4 import BeautifulSoup as bs
import os
import csv

URL = 'https://www.geeksforgeeks.org/page/1/'

'''
#first page only
req = rq.get(URL)
soup = bs(req.text, 'html.parser')
titles = soup.find_all('div')

print(titles)
'''
#multiple page

URL_without_page = 'https://www.geeksforgeeks.org/page/'

for page in range(1, 10):
    req = rq.get(URL + str(page) + '/')
    soup = bs(req.text, 'html.parser')
 
    titles_href = soup.find_all('a')
    
    titles_href_list = []
    count = 1
    for title in titles_href:
        d = {}
        d['title'] = title.text
        d['href'] = title.get('href')
        count+=1
        titles_href_list.append(d)
    
    if os.path.isdir('repos_files') == False:
        os.mkdir('repos_files')
        print('=======> repos files created <=======')
    
    filename = f'repos_files/titles_href_page{page}.csv'

    with open(filename, 'w+', newline='') as f:
        header = ['title', 'href']
        w = csv.DictWriter(f, header)
        w.writeheader()
        w.writerows(titles_href_list)
            
    print(f'=/=/=/= end page{page} =/=/=/=')
    