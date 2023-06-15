import sys, getopt 


DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 10
DEFAULT_COMMENTS_COUNT_DISABLED = False
DEFAUlt_SHOW_IN_LIST = False

def getDefaults():
    return {'page':DEFAULT_PAGE, 'per_page':DEFAULT_PER_PAGE, 'no_comment':DEFAULT_COMMENTS_COUNT_DISABLED, 'list': DEFAUlt_SHOW_IN_LIST}
    

def generateHelp():
    str1 = 'This is an example program to fetch data from https://jsonmock.hackerrank.com/api/articles. \nIt sorts articles by number of comments that they have. It will make list.'
    str2 = 'By just running it it will give you top 10 articles with most comments'
    str3 = 'Arguments with no value:'
    str4 = '-h --help \t For this help'
    str5 = '-l  --list \t Shows only article name'
    str6 = '-c  --no_comment Shows article name with its index'
    str7 = '\nArguments with value required:'
    str8 = '-p  --page \t Page number of data. Default is 1'
    str9 = '-t  --per_page \t Number of articles per page. Default is 10'
    arr = [str1, str2, str3, str4, str5, str6, str7, str8, str9]
    for x in arr:
       print(x)

def getInt(num):
    try: 
        res = int(num)
    except ValueError:
        raise ValueError
        sys.exit()
    return res



def getArgs(argv):
    opts, args = getopt.getopt(argv,'hlp:t:',['help','page=', 'per_page=','no_comment','no_comments', 'list'])
    res = getDefaults()
    for opt, arg in opts:
        if opt in ('-h','--help'):
            generateHelp()
            sys.exit()
        elif opt in ('-l', '--list'):
            res['list'] = True
        elif opt in ('--no_comment', '--no_comments'):
            res['no_comment'] = True
        elif opt in ('-p', '--page'):
            res['page'] = getInt(arg)
        elif opt in ('-t', '--per_page'):
            res['per_page'] = getInt(arg)
    return res
