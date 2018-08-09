from os import path
import sys
sys.path.append(path.abspath(".."))

import operator
from coding_challenge.datastructure.binarytree import BinaryNode, BinaryTree

EXAMPLE_TREE = ["*", "+", "+", 2, 3, 4 ,5]


operands = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "//": operator.floordiv,
        "%": operator.mod,
        "^": operator.xor
}

def getResult(startingNode, operateStack=[]):
    # if reach child node is null, that branch is done
    if startingNode is None:
        return []
    getResult(startingNode.leftNode, operateStack)
    getResult(startingNode.rightNode, operateStack)
    operateStack.append(startingNode.getValue())
    assumedOperand = operateStack.pop()
    if assumedOperand in operands:
        secondValue = operateStack.pop()
        firstValue = operateStack.pop()
        operateStack.append(operands[assumedOperand](firstValue, secondValue))
    else:
        operateStack.append(assumedOperand)
    return operateStack

def getResultFromTree(tree):
    return getResult(tree.root)[0]

def main():
    tree = BinaryTree()
    for value in EXAMPLE_TREE:
        tree.add(value)
    tree.printTree()
    print(getResultFromTree(tree))


if __name__ == "__main__":
    main()
