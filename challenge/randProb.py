from random import randint

def rand5():
    return randint(1, 5)

def rand7():
    val = (5 * rand5() + rand5() - 5)
    if val > 21:
        return rand7()
    else:
        return val%7

def main():
    probList = {}
    for _ in range(0,1000000):
        val = rand7()
        if val in probList:
            probList[val] +=1
        else:
            probList[val] = 1
    probList = {k: v/1000000 for k, v in probList.items()}
    print(probList)


if __name__ == "__main__":
    main()