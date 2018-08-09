from collections import deque

PRINT_ORDER = {
    "IN_ORDER": "IN_ORDER",
    "PRE_ORDER": "PRE_ORDER",
    "POST_ORDER": "POST_ORDER"
}

# A node in tree
class BinaryNode(object):
    def __init__(self, value, leftNode, rightNode):
        self.__value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

    def setValue(self, value):
        self.__value = value

    def getValue(self):
        return self.__value

    def printValue(self):
        return str(self.__value)


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    # return the height of a given node in tree
    def __getHeight(self, node):
        if node is None:
            return -1
        else:
            # recursively get height of its children
            lHeight = self.__getHeight(node.leftNode)
            rHeight = self.__getHeight(node.rightNode)

            # the height will be the height of the higher children + 1
            if lHeight > rHeight:
                return lHeight + 1
            else:
                return rHeight + 1

    # insertion helper (guranteed added to lowest level)
    def __insert(self, startingNode, insertingNode):
        examineNodeQueue = deque()
        examineNodeQueue.append(startingNode)
        while (len(examineNodeQueue) is not 0):
            examineNode = examineNodeQueue.popleft()
            if examineNode.leftNode is None:
                examineNode.leftNode = insertingNode
                break
            else:
                examineNodeQueue.append(examineNode.leftNode)
            if examineNode.rightNode is None:
                examineNode.rightNode = insertingNode
                break
            else:
                examineNodeQueue.append(examineNode.rightNode)
        
    # add a node in binary tree (guranteed to lowest level)
    def add(self, value):
        newDataNode = BinaryNode(value, None, None)
        if self.root is None:
            self.root = newDataNode
        else:
            self.__insert(self.root, newDataNode)

    def getList(self, startingNode, traverseOrder=PRINT_ORDER["IN_ORDER"]):
        result = []
        if startingNode is None:
            return result
        if traverseOrder == PRINT_ORDER["PRE_ORDER"]:
            result.append(startingNode.getValue())
        result += self.getList(startingNode.leftNode, traverseOrder)
        if traverseOrder == PRINT_ORDER["IN_ORDER"]:
            result.append(startingNode.getValue())
        result += self.getList(startingNode.rightNode, traverseOrder)
        if traverseOrder == PRINT_ORDER["POST_ORDER"]:
            result.append(startingNode.getValue())
        return result
    
    def getTreeList(self, traverseOrder=PRINT_ORDER["IN_ORDER"]):
        return self.getList(self.root, traverseOrder)

    # 1 is in-order, 2 is pre-order, 3 is post-order
    def printFromNode(self, startingNode, printOrder=PRINT_ORDER["IN_ORDER"], level=0):
        if startingNode is None:
            return None
        if printOrder == PRINT_ORDER["PRE_ORDER"]:
            print(("-" * level) + " " + startingNode.printValue())
        self.printFromNode(startingNode.leftNode, printOrder, level+1)
        if printOrder == PRINT_ORDER["IN_ORDER"]:
            print(("-" * level) + " " + startingNode.printValue())
        self.printFromNode(startingNode.rightNode, printOrder, level+1)
        if printOrder == PRINT_ORDER["POST_ORDER"]:
            print(("-" * level) + " " + startingNode.printValue())

    def printTree(self, printOrder=PRINT_ORDER["IN_ORDER"]):
        self.printFromNode(self.root, printOrder)


            
