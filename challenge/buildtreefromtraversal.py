from os import path
import sys
sys.path.append(path.abspath(".."))

from coding_challenge.datastructure.binarytree import BinaryNode, BinaryTree

EXAMPLE_PRE_ORDER = ["a", "b", "d", "e", "c", "f", "g"]
EXAMPLE_IN_ORDER = ["d", "b", "e", "a", "f", "c", "g"]

global currentEvalIndex
currentEvalIndex = 0

def buildTree(preOrderList, inOrderList):
    global currentEvalIndex
    if len(inOrderList) is 0:
        return None
    currentValue = preOrderList[currentEvalIndex]
    rootNode = BinaryNode(currentValue, None, None)
    try:
        currentValueInOrderIndex = inOrderList.index(currentValue)
        currentEvalIndex += 1
        rootNode.leftNode = buildTree(preOrderList, inOrderList[:currentValueInOrderIndex])
        rootNode.rightNode = buildTree(preOrderList, inOrderList[currentValueInOrderIndex:])
        return rootNode
    except:
        return None

def main():
    global currentEvalIndex
    currentEvalIndex = 0
    tree = BinaryTree(buildTree(EXAMPLE_PRE_ORDER, EXAMPLE_IN_ORDER))
    tree.printTree(printOrder="PRE_ORDER")
    

if __name__ == "__main__":
    main()
