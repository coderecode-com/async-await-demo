import asyncio


async def main(name):
    print('hello')
    await asyncio.sleep(1)
    print(name)


async def runner():
    task1 = asyncio.create_task(main('upendra'))
    task2 = asyncio.create_task(main('world'))

    await asyncio.gather(task1, task2)


asyncio.run(runner())