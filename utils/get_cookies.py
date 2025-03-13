import asyncio

import aiohttp


async def get_cookies(session):

        # Шаг 2: Переходим на страницу, чтобы получить все cookies
        summary_url = 'https://5ka.ru'
        async with session.get(summary_url) as response:
            if response.status != 200:
                raise Exception(f"Failed to fetch summary page, status code {response.status}")

        # Возвращаем все cookies
        cookies = session.cookie_jar.filter_cookies('https://5ka.ru')
        return {key: cookie.value for key, cookie in cookies.items()}

async def main():
    async with aiohttp.ClientSession() as session:
        cookies = await get_cookies(session)
        print(cookies)


if "__main__" in __name__:
    asyncio.run(main())
