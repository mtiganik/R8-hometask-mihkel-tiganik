from filter_by_comment import filterByComment
import asyncio
from argument_getter import getArgs
from resultGenerator import generateResult
import sys

url = 'https://jsonmock.hackerrank.com/api/articles'

def main(argv):
    args = getArgs(argv)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    filteredData = loop.run_until_complete(filterByComment(url, args['page'], args['per_page']))

    [header,dataToDisplay] = generateResult(filteredData, args['list'], args['no_comment'])
    print(header)
    for x in dataToDisplay:
        print(x)


if __name__ == "__main__":
    main(sys.argv[1:])