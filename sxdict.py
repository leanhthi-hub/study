def sortdict(x:dict)-> dict:
    sortedx = sorted(x.items(), key=lambda x: x[1], reverse=False)
    return sortedx

