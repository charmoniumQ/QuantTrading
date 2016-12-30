import numpy as np

def topk(newData, oldSet, k, band):
    '''Selects the top k elements from newData where k is the length of the oldSet
    An item will be added if its rank falls below the k - band.
    An item will be removed if its rank rises above the k + band
    If there are too many items, the worst will be removed.
    If there are too few items, the best will be added.

    newData: numpy array()
    oldSet: python set()
    k: integer
    band: integer
    returns a set'''
    ranking = rank(newData)
    newSet = set()

    # retain old ones that haven't fallen below the threshold
    for x in oldSet:
        if ranking[x] < k + band:
            newSet.add(x)

    # add new ones that have risen above the threshold
    for x in ranking[:k - band]:
        newSet.add(x)

    while len(newSet) > k:
        # we have added too many, take out the largest in the set
        maxx = max([(ranking[x], x) for x in newSet])[1]
        newSet.remove(maxx)

    while len(newSet) < k:
        # we have added too few, add the smallest not in the set
        minx = min([(ranking[x], x) for x in range(0, len(newData)) if x not in newSet])[1]
        newSet.add(minx)

    return newSet

def invert(array):
    '''An array where
    0 -> 1
    1 -> 3
    2 -> 0
    3 -> 2
    will convert to an array where
    0 -> 2
    1 -> 0
    2 -> 3
    3 -> 1'''
    result = np.zeros(len(array), dtype=np.int64)
    for i, v in enumerate(array):
        result[v] = i
    return result

def rank(array):
    return invert(array.argsort())

if __name__ == '__main__':
    k = 4
    band = 2
    currentSet = set()

    data = invert([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    currentSet = topk(data, currentSet, k, band)
    assert currentSet == {0, 1, 2, 3}, 'the indexes of the highest values: ' + str(currentSet)

    data = invert([0, 1, 4, 5, 2, 3, 6, 7, 8, 9])
    currentSet = topk(data, currentSet, k, band)
    assert currentSet == {0, 1, 2, 3}, 'keep if falls out of top k, but within band: ' + str(currentSet)

    data = invert([0, 1, 4, 5, 6, 7, 8, 9, 2, 3])
    currentSet = topk(data, currentSet, k, band)
    assert currentSet == {0, 1, 4, 5}, 'throw out if falls out of top k and band (also 2 values keep 4): ' + str(currentSet)

    data = invert([2, 3, 0, 1, 4, 5, 6, 7, 8, 9])
    currentSet = topk(data, currentSet, k, band)
    assert currentSet == {2, 3, 0, 1}, 'if 6 values, keep the 4 highest: ' + str(currentSet)

    print('all tests run')

__all__ = ['topk']
