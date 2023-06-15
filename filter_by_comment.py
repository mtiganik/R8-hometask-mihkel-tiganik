import requests
import aiohttp
import json
import asyncio

def appendToResData(title,comments):
    return {
        'title':title,
        'num_comments': comments
    }

def getUrls(url, pageCnt):
    urls = []
    for i in range(pageCnt):
        urls.append(f'{url}?page={i+1}')
    return urls

def createDTO(res, page, per_page):
    res = [item for sublist in res for item in sublist]
    res.sort(key=lambda x: x.get('num_comments'), reverse=True) 
    res = res[per_page*(page-1):per_page*page]
    for i,x in enumerate(res):
        x['index'] = per_page*(page-1) + i+1
    return res

def singlePageJSON(data):
    resData = []
    for x in data:
        if x['num_comments']: 
            if x['title']: resData.append(appendToResData(x['title'], x['num_comments']))
            elif x['story_title']: resData.append(appendToResData(x['story_title'], x['num_comments']))
    return resData

async def getPageCnt(url):
    r = requests.get(url)
    pageCnt = r.json()['total_pages']
    return pageCnt

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def filterByComment(url,page,per_page=10):
    pageCnt = await getPageCnt(url)
    urls = getUrls(url, pageCnt)
    tasks,res = [],[]
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, url))
        JSONs = await asyncio.gather(*tasks)
        for JSON in JSONs:
            res.append(singlePageJSON(json.loads(JSON)['data']))
    return createDTO(res,page,per_page)


