import asyncio


async def main(name):
    print('hello')
    await asyncio.sleep(1)
    print(name)


loop = asyncio.get_event_loop()
loop.run_until_complete(main('Upendra'))
# loop.run_until_complete(main('World'))
loop.close()
