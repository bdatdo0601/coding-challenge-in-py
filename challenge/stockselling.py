from highestsubsetsum import getHighestSumOfSubset

EXAMPLE_LIST = [9, 11, 8, 5, 7, 10, 80, 60, 10, 20, 50,70]

# The idea is to get the difference between the each price point
# the most profitable time to buy and sell will be the largest contageous
# sum of those difference

# gonna use kadane algorithm to find largest contageous sum

def getMostOptimalTrade(priceList):
    if (len(priceList) <= 1):
        return (None, None, 0)
    differenceList = []
    for i in range(1, len(priceList)):
        differenceList.append(priceList[i] - priceList[i-1])

    # Kadane algorithm
    # max_ends_here = 0
    # max_so_far = 0
    # endingIndex = None
    # for (index, value) in enumerate(differenceList):
    #     max_ends_here = max(value, max_ends_here + value)
    #     current_max_so_far = max_so_far
    #     max_so_far = max(max_ends_here, max_so_far)
    #     if current_max_so_far is not max_so_far:
    #         endingIndex = index + 1
    # if endingIndex is not None:
    #     startingIndex = endingIndex - 1
    #     currentTotal = differenceList[startingIndex]
    #     while (currentTotal != max_so_far and startingIndex > 0):
    #         startingIndex -= 1
    #         currentTotal += differenceList[startingIndex]

    (startingIndex, endingIndex, max_so_far) = getHighestSumOfSubset(differenceList)
    
    return (priceList[startingIndex], priceList[endingIndex], startingIndex, endingIndex, max_so_far)

def main():
    print(getMostOptimalTrade(EXAMPLE_LIST))


if __name__ == "__main__":
    main()
