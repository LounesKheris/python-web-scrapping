import requests
from bs4 import BeautifulSoup

#request : Get method
URL = 'https://www.geeksforgeeks.org/python-programming-language/'
r = requests.get(URL)

#check response

if r.status_code==200:
    soup = BeautifulSoup(r.content,'html.parser')
    leftbarparent = soup.find('ul', class_='leftBarList')
    leftbarlist = leftbarparent.find_all('li')

    #extract links
    for link in soup.find_all('a'):
        link_ = link.get('href')
        #print(link_)

    #extract images
    img_list = []
    images = soup.select('img')
    for img in images:
        src = img.get('src')
        alt = img.get('alt')
        img_list.append({"src":src,"alt":alt})
    
    for image in img_list:
        print('\n',image)
else:
    print('Error : ',r.status_code)