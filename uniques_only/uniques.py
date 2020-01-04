def uniques_only(lst):
    resultlst = []
    resultSet = set()
    for item in lst:
        try:
            if item in resultSet:
                pass
            else:
                yield item
                resultSet.add(item)
        except:
            if item in resultlst:
                pass
            else:
                yield item
                resultlst.append(item)
