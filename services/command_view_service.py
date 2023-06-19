
def generateListData(data):
    header = "---------Result---------"
    res = []
    for x in data:
        res.append(f"  {x['title']}")
    return [header,res]

def generateWithoutComments(data):
    header = ' ID \tTitle'
    res = []
    for x in data:
        str = f" {x['index']} \t{x['title']}"
        res.append(str)
    return [header,res]

def stringInComment(str):
    res = str
    strLen = len(str)
    for i in range(1,8):
        if strLen < i*8:
            return res + '\t'*(8-i)
    if strLen > 55:
        return res[:52] + "...\t"
    return res[:55]

def generateWithComments(data):
    header = "ID\tTitle\t\t\t\t\t\t\tComments"
    res = []
    for x in data:
        str = f"{x['index']} \t{stringInComment(x['title'])}{x['num_comments']}"
        res.append(str)
    return [header,res]

def generateResult(data, isList, noComments):
    if isList:
        return generateListData(data)
    if noComments:
        return generateWithoutComments(data)
    else:
        return generateWithComments(data)
    



