import requests
import time 
import asyncio

url = 'https://jsonmock.hackerrank.com/api/articles'

# if more stuff is needed to DTO insert them here
def appendDataToDTO(title,comments):
    return {
        'title':title,
        'num_comments': comments
    }


async def dataFromPage(pageNum):
    r = requests.get(f'{url}?page={pageNum}')
    data = r.json()['data']
    resData = []
    for x in data:
        if x['num_comments']: 
            if x['title']: resData.append(appendDataToDTO(x['title'], x['num_comments']))
            elif x['story_title']: resData.append(appendDataToDTO(x['story_title'], x['num_comments']))
    return resData
        


async def retrieveData(url,page, per_page=10):
    r = requests.get(url)
    pageCnt = r.json()['total_pages']
    res = await asyncio.gather(*(dataFromPage(i) for i in range(1,pageCnt)))
    
    res = [item for sublist in res for item in sublist]
    res.sort(key=lambda x: x.get('num_comments'), reverse=True) 
    res = res[per_page*(page-1):per_page*page]

    return [x['title'] for x in res]

data = asyncio.run(retrieveData(url,page=1,per_page=10))
