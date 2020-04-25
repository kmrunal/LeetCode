# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]


# Time Complexity: O(N^2), where N is the number of nodes.
# Space Complexity: O(N^2)

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root

        L = post.index(pre[1]) + 1

        root.left = self.constructFromPrePost(pre[1:L+1],post[:L])
        root.right = self.constructFromPrePost(pre[L+1:],post[L:])

        return root
