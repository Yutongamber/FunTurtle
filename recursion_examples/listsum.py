def listsum(numlist):
    if len(numlist) == 1:
        results = numlist[0]
        print("check 1: ", results)
        return results
    else:
        results = numlist[0] + listsum(numlist[1:])
        print("check: ", results)
        return results

numList = [1,3,5,7,9]
listsum(numList)
