# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def traversalNode(self, node, value):
        if node is None:
            return 0
        valueGst = self.traversalNode(node.right,value)
        val = node.val
        node.val = valueGst+val
        valueresult= self.traversalNode(node.left,valueGst+val)
        return valueresult
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:
            return 0
        value = 0
        valueresult = self.traversalNode(root,value)
        print(valueresult)
        return root

if __name__ == "__main__":
    pass