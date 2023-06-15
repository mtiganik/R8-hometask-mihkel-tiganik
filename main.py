from filter_by_comment import filterByComment
import asyncio


url = 'https://jsonmock.hackerrank.com/api/articles'

if __name__ == "__main__":
    page = 1
    entriesPerPage = 10
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(filterByComment(url, page, entriesPerPage))
    for x in result:
        print(x)

