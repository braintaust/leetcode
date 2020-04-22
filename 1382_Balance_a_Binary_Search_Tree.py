# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inOrderTras(self,node,sortArray):
        if node is None:
            return
        self.inOrderTras(node.left,sortArray)
        sortArray.append(node.val)
        self.inOrderTras(node.right,sortArray)

    def newTreeNode(self,i,h,array):
        if i>h:
            return None
        m  = math.floor((i+h)/2)
        node = TreeNode(array[m])
        node.left  = self.newTreeNode(i,m-1,array)
        node.right = self.newTreeNode(m+1,h,array)
        return node
        
    def newTree(self,array):
        m  = math.floor((len(array)-1)/2)
        root  = TreeNode(array[m])
        root.left = self.newTreeNode(0,m-1,array)
        root.right = self.newTreeNode(m+1,len(array)-1,array)
        return root
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sortArray = []
        self.inOrderTras(root,sortArray)
        print(sortArray)
        node = self.newTree(sortArray)
        return node
        
