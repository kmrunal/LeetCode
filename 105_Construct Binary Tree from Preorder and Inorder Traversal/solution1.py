# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# ans_level_order = [[3,9,20,null,null,15,7]]


# Time Complexity: O(N^2), where N is the number of nodes.
# Space Complexity: O(N^2)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        middle = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:middle+1], inorder[:middle])
        root.right = self.buildTree(preorder[middle + 1:], inorder[middle + 1:])
        return root
