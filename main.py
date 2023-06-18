from filter_by_comment import filterByComment
import asyncio
from argument_getter import getArgs
from constants import getUrl
from resultGenerator import generateResult
import sys


def main(argv):
    args = getArgs(argv)
    url = getUrl()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    filteredData = loop.run_until_complete(filterByComment(url, args['page'], args['per_page']))

    [header,dataToDisplay] = generateResult(filteredData, args['list'], args['no_comment'])
    print(header)
    for x in dataToDisplay:
        print(x)


if __name__ == "__main__":
    main(sys.argv[1:])