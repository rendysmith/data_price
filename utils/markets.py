import asyncio
import time

import aiohttp
import requests
from bs4 import BeautifulSoup

from utils.get_cookies import get_cookies

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


async def get_data_5ka(url):
    params = {
        "mode": "delivery",
        "include_restrict": "true"
    }
    # Заголовки запроса
    headers = {
        "Host": "5d.5ka.ru",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "X-DEVICE-ID": "bef84d28-7822-4be0-a3d3-adc89b694eba",
        "X-APP-VERSION": "tc5-v250312-31214353",
        "X-PLATFORM": "webapp",
        "Origin": "https://5ka.ru",
        "DNT": "1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Connection": "keep-alive",
        "TE": "trailers"
    }


    print('\n',url)

    async with aiohttp.ClientSession() as session:
        # Куки
        cookies = await get_cookies(session)
        for key, value in cookies.items():
            cook_key = key
            cook_value = value

        print(cookies)
        cookies = {
            "TS01658276": "01a2d8bbf4a22e516c628fcf8e03e6a7c15ef7c31d6211b77ae9ed5208cfab588b1ad0dec18ace424b09e3a13966c5b79a69334084",
            "spid": "1741850199112_c4e88c2ee7391efa0da9a549be69972a_a0kokt6du9rfcslp",
            "spsc": "1741850199112_32292726e7f987598f888a29a43f095f_e6cfb3ea8f0a0fa28cc6ebefdcae8ea5",
            "SRV": "f77ae7c7-38be-4ff6-9d30-274349ccc5a2",
            cook_key: cook_value}

        async with session.get(url, params=params, headers=headers, cookies=cookies) as response:
            if response.status == 200:
                try:
                    r_json = await response.json()
                    print(r_json)

                except Exception as Ex:
                    print(f"Error Ex: {Ex}\n{await response.text()}")

            else:
                print(f'Status: {response.status}')
                print(await response.text())






async def main():
    link = 'https://5ka.ru/product/moloko-selo-zelenoe-pasterizovannoe-3-2-bzmzh-1-94--3425329/'
    await get_data_5ka(link)


if "__main__" in __name__:
    #link = 'https://5ka.ru/product/moloko-selo-zelenoe-pasterizovannoe-3-2-bzmzh-1-94--3425329/'
    asyncio.run(main())

