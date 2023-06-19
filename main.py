import sys
import asyncio
from constants import getUrl
from services.comment_filter_service import filterByComment
from services.argument_service import getArgs
from services.command_view_service import generateResult


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