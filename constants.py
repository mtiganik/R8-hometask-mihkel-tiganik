DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 10
DEFAULT_COMMENTS_COUNT_DISABLED = False
DEFAUlt_SHOW_IN_LIST = False

URL = 'https://jsonmock.hackerrank.com/api/articles'

def getDefaults():
    return {'page':DEFAULT_PAGE, 'per_page':DEFAULT_PER_PAGE, 'no_comment':DEFAULT_COMMENTS_COUNT_DISABLED, 'list': DEFAUlt_SHOW_IN_LIST}


def getUrl():
    return URL