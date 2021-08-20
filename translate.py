# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

while(1):
    print('>> ', end='')
    en = input()
    en.replace(' ','+')
    
    res = requests.get('https://ejje.weblio.jp/content/{}'.format(en))
    
    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        ja = soup.find(class_='content-explanation')
        print(ja.get_text())
    except:
        print('「{}」に一致する見出し語が見つかりません。'.format(en))
        
    print('')



