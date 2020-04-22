# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        queue=[root]
        result = []
        while queue:
            next_queue=[]
            his = True
            for n in queue:
                if n is None:
                    continue
                if his:
                    result.append(n.val)
                    his = False
                next_queue.append(n.right)
                next_queue.append(n.left)
        return result
