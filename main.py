import asyncio
import time
import threading
from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3

from utils.markets import main

import os
print(os.getcwd())
print('***********************')

# url = 'https://online.metro-cc.ru/category/molochnye-prodkuty-syry-i-yayca/moloko/prostokvashino-pasterizovannoe-25-093-l'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# r = requests.get(url, headers=headers)
# print(r.text)
# input()

# conn = sqlite3.connect(:memory:) #создание БД в оперативной памяти
conn = sqlite3.connect('goods_db.db')  # создание БД если нет. Если есть то подключение.
cur = conn.cursor()

db_name = 'goods_stat_tbl'

cur.execute(f"""CREATE TABLE IF NOT EXISTS {db_name}(
unix_date INT,
name_goods TEXT,
price REAL,
link TEXT,
art TEXT);
""")
conn.commit()

df = pd.read_sql(f'SELECT * FROM {db_name}', conn)
print('Записей в базе', len(df))




        # name_item = soup.find('h1', attrs={'itemprop' : 'name'})
        # print(name_item)

while True:
    df = pd.read_csv('data.csv')

    for i, row in df.iterrows():
            link = row[0]
            asyncio.run(main())
            #threading.Thread(target=get_data, args=(link,)).start()
            time.sleep(5)

    ts = 82800
    print(f'Wait {ts} sec.')
    time.sleep(ts)







