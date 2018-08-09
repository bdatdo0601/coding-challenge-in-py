from random import randint

CARDS=[x for x in range(0, 52)]

def getRandom(toValue):
    return randint(0, toValue - 1)

def shuffleDeck(cards):
    for i in range(0, len(cards)):
        cardToSwapWithIndex = getRandom(len(cards) - i) + i
        cards[i], cards[cardToSwapWithIndex] = cards[cardToSwapWithIndex], cards[i]


if __name__=="__main__":
    print(CARDS)
    shuffleDeck(CARDS)
    print(CARDS)