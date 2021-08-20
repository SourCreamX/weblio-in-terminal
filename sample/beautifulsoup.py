import requests
from bs4 import BeautifulSoup


# スクレイピングするURLを指定しHTMLを取得    
res = requests.get('https://ejje.weblio.jp/content/apple')

# BeautifulSoupオブジェクトをつくる
soup = BeautifulSoup(res.text, 'html.parser')

# クラス名を指定して要素を取得
print(soup.select("[class_='content-explanation']").get_text())




