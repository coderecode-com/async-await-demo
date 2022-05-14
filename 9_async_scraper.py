import csv
import re

import aiohttp
import asyncio
import time

start_time = time.time()


def get_links():
    links = []
    with open('links.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            links.append(row[0])
    return links


async def get_response(session, url):
    async with session.get(url) as resp:
        text = await resp.text()
        exp = r'(<title>).*(<\/title>)'
        return re.search(exp, text).group(0)


async def main():
    async with aiohttp.ClientSession() as session:

        tasks = []
        for url in get_links():
            tasks.append(asyncio.create_task(get_response(session, url)))

        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
