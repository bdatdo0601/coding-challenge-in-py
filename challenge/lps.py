def getLongestPalindromeSubstring(string):
    dimension = len(string)
    checkTable = [[False for _ in range(dimension)] for _ in range(dimension)]
    lpsLength = 0
    startingIndex = None
    endingIndex = None
    for i in range(dimension-1, 0, -1):
        for j in range(i, dimension):
            if i == j:
                checkTable[i][j] = True
            elif (i + 1) > (j - 1):
                checkTable[i][j] = True if string[i] == string[j] else False
            else:
                checkTable[i][j] = True if string[i] == string[j] and checkTable[i+1][j-1] else False
            if checkTable[i][j]:
                if lpsLength < (j - i):
                    lpsLength = j - i
                    startingIndex = i
                    endingIndex = j
    
    return (string[startingIndex:endingIndex + 1], startingIndex, endingIndex)


if __name__ == "__main__":
    print(getLongestPalindromeSubstring("aabcdcb"))
            
