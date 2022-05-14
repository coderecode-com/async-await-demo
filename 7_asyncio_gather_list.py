import asyncio


async def main(name):
    print('hello')
    await asyncio.sleep(1)
    print(name)


async def runner():
    names = ['upendra', 'world']

    tasks = []
    for name in names:
        tasks.append(asyncio.create_task(main(name)))

    await asyncio.gather(*tasks)


asyncio.run(runner())
