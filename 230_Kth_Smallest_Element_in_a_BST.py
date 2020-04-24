# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 进阶：
# 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
# 这个进阶需要修改树节点的数据结构，要求每个树节点分别记录左子节点和右子节点的数量
#    查找第 k 小的值，先判断左子节点数量，大于左子节点数量+1，则去右侧，并且k-右子节点数量；
#    小于等于左子节点数量则去左侧，如果等于左子节点数量+1,返回此节点。
# 插入的时候，向右侧则右侧节点+1，向左侧则左侧节点+1
# 删除的时候，找到右侧最小值补入，该节点修改左侧子节点数量和右侧子节点数量
# 如果不修改节点的数据结构，需要节点下左右子节点数量进行解决，仍然是O(N)


class Solution:
    def inOrder(self,node,cnts):
        if node is None:
            return
        self.inOrder(node.left,cnts)
        if cnts[0] > 0 :
            cnts[0] = cnts[0] - 1
        if cnts[0] == 0:
            cnts[0] = cnts[0] - 1
            cnts[1] = node.val
            return
        if cnts[0] < 0:
            return
        self.inOrder(node.right,cnts)
    def kthSmallest(self, root, k):
        #中序遍历
        res = [k,root.val]
        self.inOrder(root,res)
        return res