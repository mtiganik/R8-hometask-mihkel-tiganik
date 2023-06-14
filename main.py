import requests

url = 'https://jsonmock.hackerrank.com/api/articles?page='
currPage = 1
r = requests.get(url + str(currPage))

json = r.json()
data,total_pages = json['data'], json['total_pages']
print(total_pages)
