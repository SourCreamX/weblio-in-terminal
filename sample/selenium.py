import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument('--headless')
driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=option)

print("---------------------- 英和辞書 --------------------------")

while(1):
    print(">> ",end='')
    en = input()
    en.replace(' ','+')
    '''
    #google翻訳
    driver.get('https://translate.google.com/?sl=en&tl=ja&text={}%0A&op=translate'.format(en))
    time.sleep(1)
    ja = driver.find_element_by_css_selector("span[jsname='W297wb']")
    print(ja.text)
    '''

    #weblio
    driver.get('https://ejje.weblio.jp/content/{}'.format(en))
    time.sleep(1)
    try:
        ja = driver.find_element_by_class_name('content-explanation')
        print(ja.text)
    except:
        print('{}に一致する見出し語が見つかりません。'.format(en))

    
    print("")
    

