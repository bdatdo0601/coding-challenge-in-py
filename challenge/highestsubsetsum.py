EXAMPLE_LIST_1 = [34, -50, 42, 14, -5, 86]
EXAMPLE_LIST_2 = [-5, -1, -8, -9]

# The idea is to have an inductive algorithm, taking
# advantage of the subset will surely end at in index i < N
# by slowly increasing problem size, we can find the maximum, or minimum sum

# Initialization, max_end_here & max_so_far will be initialize as first index (or 0)
# since we only check first element, we know that either this or empty array is max value,
#

# Invariants, for every iteration, we add in another element and compare the sum of it and max_end_here
# current with max_end_here. *IMPORTANT* we know that the maximum sum of subarray ending at index i will always 
# be the maximum of subarray at index i-1, so we only need to compare the value at i versus the total of the max of subarray
# at index i - 1 with value (ensuring invariant of max_end_here)
# Thus max_end_here will always hold true. 
# since we will know maximum of subarray ending of at least the current iterating position,
# max_so_far will always keep track of the highest sum

# Termination, the algo will terminate when iteration ends, max_so_far will hold the highest sum recorded

def getHighestSumOfSubset(valueList):
    max_end_here = 0
    max_so_far = 0
    endingIndex = None
    for (index, value) in enumerate(valueList):
        max_end_here = max(value, max_end_here + value)
        current_max_so_far = max_so_far
        max_so_far = max(max_end_here, max_so_far)
        if (current_max_so_far != max_so_far):
            endingIndex = index + 1
    
    # extra to store starting index
    if (endingIndex is not None):
        startingIndex = endingIndex - 1
        currentTotal = valueList[startingIndex]
        while (currentTotal < max_so_far and startingIndex > 0):
            startingIndex -= 1
            currentTotal += valueList[startingIndex]
    else:
        startingIndex = None
    
    return (startingIndex, endingIndex, max_so_far)


if __name__ == "__main__":
    print(getHighestSumOfSubset(EXAMPLE_LIST_1))
    print(getHighestSumOfSubset(EXAMPLE_LIST_2))
