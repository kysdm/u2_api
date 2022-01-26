# -*- coding: utf-8 -*-

import os
import sys
import aiohttp
import asyncio
import aiofiles
from aiocsv import AsyncWriter
from loguru import logger

'''
Python3.9.9
aiocsv==1.2.1
aiofiles==0.8.0
aiohttp==3.8.1
loguru==0.5.3
'''

UID = ''
TOKEN = ''


class API():
    def __init__(self):
        self.session = None

    async def get(self, url: str) -> dict:
        if self.session is None:
            self.session = aiohttp.ClientSession()
        for i in range(15):
            try:
                timeout = aiohttp.ClientTimeout(total=80, sock_connect=15, sock_read=45)
                async with self.session.get(url, timeout=timeout) as resp:
                    if resp.status < 300:
                        return await resp.json()
                    else:
                        logger.error(f'状态码不正确<{resp.status}> * {i} | 10秒后重试... | {url}')
                        await asyncio.sleep(3)
            except asyncio.TimeoutError as e:
                logger.error(f'超时 * {i} | 10秒后重试... | {url} | {e}')
                await asyncio.sleep(10)
            except Exception as e:
                logger.error(f'发生致命错误 | 30秒后重试... | {url} | {e}')
                await asyncio.sleep(30)

    async def close(self) -> None:
        if self.session is not None:
            await self.session.close()


async def save(lock: object, tid: str, title: str, subtitle: str) -> None:
    async with lock:
        async with aiofiles.open(os.path.join(abs_path, 'id.csv'), "a", encoding="utf-8-sig", newline='') as f:
            writer = AsyncWriter(f, dialect="excel")
            await writer.writerow([tid, title, subtitle])


async def process(tid: str, sem: object, lock: object) -> None:
    async with sem:
        __json = await api.get(f'https://u2.kysdm.com/api/v1/history/?token={TOKEN}&maximum=1&uid={UID}&torrent={tid}')
        if __json['state'] == '200':
            logger.debug(f'#{tid} 成功获取')
            __data = __json['data']['history']
            if len(__data) == 0:
                logger.warning(f'#{tid} 没有数据')
            else:
                title = __data[0]['title']
                subtitle = '' if __data[0]['subtitle'] is None else __data[0]['subtitle']
                await save(lock, tid, title, subtitle)
        else:
            logger.error(f'#{tid} JSON 内状态码错误')


async def main(id_list: list) -> None:
    sem = asyncio.Semaphore(20)
    lock = asyncio.Lock()
    tasks = [asyncio.create_task(process(_, sem, lock)) for _ in id_list if _ != '']
    await asyncio.gather(*tasks)
    await api.close()


if __name__ == "__main__":
    api = API()
    abs_path = os.path.split(os.path.realpath(__file__))[0]
    logger.add(level='WARNING', sink=os.path.join(abs_path, 'error.log'), encoding='utf-8')

    with open(os.path.join(abs_path, 'id.txt'), 'r', encoding="utf-8") as f:
        f1 = f.read().split('\n')
        if sys.platform == 'win32':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(main(sorted(set(f1), key=f1.index)))
