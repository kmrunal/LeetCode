# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, root):
        d = 0
        while root.left:
            root = root.left
            d += 1
        return d

    def exists(self, root, d, ind):
        left = 0
        right = 2**d - 1

        node = root

        while left < right:
            pivot = left + (right - left) // 2
            if ind <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1

        return node

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = self.getDepth(root)
        if depth == 0:
            return 1

        left = 0
        right = 2**depth - 1

        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(root, depth, pivot):
                left = pivot + 1
            else:
                right = pivot - 1

        return ( 2**depth - 1 ) + left


        
