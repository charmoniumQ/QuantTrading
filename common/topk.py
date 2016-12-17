def topk(newData, oldSet, band):
    '''Selects the top k elements from newData where k is the length of the oldSet
    An item will be added if its rank falls below the k - band.
    An item will be removed if its rank rises above the k + band
    If there are too many items, the worst will be removed.
    If there are too few items, the best will be added.

    newData: numpy array()
    oldSet: python set()
    band: integer
    returns a set'''
    ranking = newData.argsort()
    newSet = set()

    # retain old ones that haven't fallen below the threshold
    for x in oldSet:
        if ranking[x] < len(oldSet) + band:
            newSet.add(x)

    # add new ones that have risen above the threshold
    for x in ranking[:len(oldSet) - band]:
        newSet.add(x)

    while len(newSet) > len(oldSet):
        # we have added too many, take out the largest in the set
        maxx = max([(ranking[x], x) for x in newSet])[1]
        newSet.remove(maxx)

    while len(newSet) < len(oldSet):
        # we have added too few, add the smallest not in the set
        minx = min([(ranking[x], x) for x in range(0, len(newData)) if x not in newSet])[1]
        newSet.add(minx)

    return newSet

__all__ = ['topk']
