# the simple way is brute force every single 
# pair combination --> O(N^2)

# by utilizing merge sort, we can increase efficiency to O(N*LOG(N))

# The idea is to count inversion when merging subarrays
# (every time when a left subarray index greater than right subarray index)
# the number of inversion will be equal to the cutting point (mid) minus 
# left subarray index (since we know all the element behind it will be greater
# per merge sort property)
EXAMPLE_LIST = [1, 3, 5,4,3,2,1]

def merge(leftIndex, middleIndex, rightIndex, array, inversionCount, inversionPairs):
    i = leftIndex
    j = middleIndex
    tempArr = []
    while (len(tempArr) != rightIndex - leftIndex):
        if (i >= middleIndex and j < rightIndex):
            tempArr += [ array[k] for k in range(j, rightIndex) ]
        elif (j >= rightIndex and i < middleIndex):
            tempArr += [ array[k] for k in range(i, middleIndex) ]
        elif (array[i] <= array[j]):
            tempArr.append(array[i])
            i += 1
        else:
            tempArr.append(array[j])
            # OPTIONAL: GET ALL PAIRS
            for k in range(i, middleIndex):
                inversionPairs.append((array[k], array[j]))
            inversionCount += middleIndex - i
            j += 1
    # Copy array
    for k in range(leftIndex, rightIndex):
        array[k] = tempArr[k - leftIndex]
    return inversionCount

def mergeSort(leftIndex, rightIndex, array, inversionPairs=[], inversionCount=0):
    if ((rightIndex - leftIndex) > 1):
        middleIndex = leftIndex + (rightIndex - leftIndex)/2
        (invCountLeft, _) = mergeSort(leftIndex, middleIndex, array, inversionPairs, inversionCount)
        inversionCount = invCountLeft
        (invCountRight, _) = mergeSort(middleIndex, rightIndex, array, inversionPairs, inversionCount)
        inversionCount= invCountRight
        inversionCount = merge(leftIndex, middleIndex, rightIndex, array, inversionCount, inversionPairs)
    return (inversionCount, inversionPairs)

def findInversion(array):
    return mergeSort(0, len(array), array)

if __name__=="__main__":
    print(EXAMPLE_LIST)
    print(findInversion(EXAMPLE_LIST))
    print(EXAMPLE_LIST)

