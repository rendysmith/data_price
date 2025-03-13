import asyncio
import time

import requests
from bs4 import BeautifulSoup

from utils.user_agent import get_selenium_proxy


async def get_data_perekrestok(link):
    print('\n',link)
    page = requests.get(link)
    print(page)

    try:
        soup = BeautifulSoup(page.text, "html.parser")

        title = soup.find('h1', attrs={'itemprop': "name"})
        name_item = title.text

        block = soup.find('div', class_ = 'product-price-wrapper')
        price = block.find('div', class_ = 'price-new').text
        price = float(price.split(' ₽')[0].replace(',', '.'))

        print(f'Price = {price}')

        art = link.split('-')[-1]

        data_list = [int(time.time()), name_item, price, art, link]
        cur.execute(f"INSERT INTO {db_name} VALUES(?, ?, ?, ?, ?);", data_list)
        conn.commit()
        print(f'+++ {name_item} Commit!')

    except:
        print(f'-ERROR- {link}')


async def get_data_5ka(link):
    driver = await get_selenium_proxy(link, proxy=False)
    print(driver.page_source)


async def main():
    link = 'https://5ka.ru/product/moloko-selo-zelenoe-pasterizovannoe-3-2-bzmzh-1-94--3425329/'
    await get_data_5ka(link)


if "__main__" in __name__:
    #link = 'https://5ka.ru/product/moloko-selo-zelenoe-pasterizovannoe-3-2-bzmzh-1-94--3425329/'
    asyncio.run(main(link))

