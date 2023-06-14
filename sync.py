import requests
import time 
# if more stuff is needed to DTO insert them here
def appendDataToDTO(title,comments):
    return {
        'title':title,
        'num_comments': comments
    }

# business logic to retrieve correct data
def addValidData(data, dataDTO):
    for x in data:
        if x['num_comments']: 
            if x['title']: dataDTO.append(appendDataToDTO(x['title'], x['num_comments']))
            elif x['story_title']: dataDTO.append(appendDataToDTO(x['story_title'], x['num_comments']))
    dataDTO.sort(key=lambda x: x.get('num_comments'), reverse=True)
    return dataDTO

url = 'https://jsonmock.hackerrank.com/api/articles'

def retrieveData(url):
    page= '?page='
    dataDTO = []
    hasPageCntSet = False
    pageCnt,i = 0,1
    while True:
        r = requests.get(f"{url}{page}{i}")
        dataDTO = addValidData(r.json()['data'], dataDTO) 
        if not hasPageCntSet:
            pageCnt = r.json()['total_pages']
            hasPageCntSet = True
        i += 1
        if i >= pageCnt:
            break

    # return dataDTO[:10]
    result = []
    for i in range(10):
        result.append(dataDTO[i]['title'])
        result.append(dataDTO[i])

    return result

start = time.perf_counter()
data = retrieveData(url)
end = time.perf_counter()

for x in data:
    print(x)

print(end-start)