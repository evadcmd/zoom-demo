import aiohttp
import logging

logging.basicConfig(level=logging.DEBUG)
# TODO: find out why it does not work
logging.getLogger("aiohttp.client").setLevel(logging.DEBUG)


async def post(url, headers, data=None, json=None):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data, json=json) as resp:
            data = await resp.json()
            return resp.status, data
