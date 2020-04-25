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
        def helper(i, j , N):
            if N == 0:
                return None

            root = TreeNode(pre[i])
            if N == 1:
                return root

            for L in range(N):
                if post[j + L - 1] == pre[i + 1]:
                    break

            root.left = helper(i+ 1, j, L)
            root.right = helper(i + L + 1, j + L, N - L -1)
            return root


        return helper(0, 0, len(pre))
