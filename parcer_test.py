# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:55:12 2020

@author: Admin
"""
'''
pip install user_agent
'''

import requests
from bs4 import BeautifulSoup
import re
import os

# library to generate user agent
from user_agent import generate_user_agent
# generate a user agent
headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}

page_response = requests.get('https://www.ozon.ru/category/ortopedicheskie-podushki-31148/', timeout=5, headers=headers)

#page_response = requests.get('https://www.ozon.ru/seller?category=14500', timeout=5, headers=headers)
path_now=os.getcwd()
#URL=input ('Введи URL который хочешь спарсить : \n')
name_folder=input ('Введи название папки : \n')
os.mkdir(name_folder)
#page=requests.get(URL)
soup=BeautifulSoup(page_response.content, 'html.parser')
print(soup.prettify())
results=soup.find_all('img', src=re.compile('https?:\/\/\S+(?:jpg|jpeg)'))
print(results)

for i in range(len(results)):
    link=results[i]['src']
    print(link)
    img_data=requests.get(link)
    print(img_data.content)
    with open (name_folder+'/'+str(i)+'.jpg','wb') as handler:
        handler.write(img_data.content)