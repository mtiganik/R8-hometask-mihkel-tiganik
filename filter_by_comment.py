import requests
import asyncio
import aiohttp
import json

def appendToResData(title,comments):
    return {
        'title':title,
        'num_comments': comments
    }
async def getPageCnt(url):
    r = requests.get(url)
    pageCnt = r.json()['total_pages']
    return pageCnt

async def createDTO(res, page, per_page=10):
    res = [item for sublist in res for item in sublist]
    res.sort(key=lambda x: x.get('num_comments'), reverse=True) 
    res = res[per_page*(page-1):per_page*page]
    return [x['title'] for x in res]

async def singlePageJSON(data):
    resData = []
    for x in data:
        if x['num_comments']: 
            if x['title']: resData.append(appendToResData(x['title'], x['num_comments']))
            elif x['story_title']: resData.append(appendToResData(x['story_title'], x['num_comments']))
    return resData

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

url = 'https://jsonmock.hackerrank.com/api/articles'

def getUrls(url, pageCnt):
    urls = []
    for i in range(1,pageCnt):
        urls.append(f'{url}?page={i}')
    return urls

async def main(url,page,per_page=10):
    pageCnt = await getPageCnt(url)
    urls = getUrls(url, pageCnt)
    tasks,res = [],[]
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, url))
        JSONs = await asyncio.gather(*tasks)
        for JSON in JSONs:
            res.append(await singlePageJSON(json.loads(JSON)['data']))
    return await createDTO(res,2,10)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main(url, page=1))
    for x in result:
        print(x)
