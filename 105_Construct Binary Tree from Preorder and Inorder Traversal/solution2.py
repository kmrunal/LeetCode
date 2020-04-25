# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# ans_level_order = [[3,9,20,null,null,15,7]]

# Time Complexity: O(N), where N is the number of nodes.
# Space Complexity: O(N)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.pre_index = 0
        def helper(in_left = 0, in_right = len(inorder)):
            if in_left == in_right:
                return None

            root_val = preorder[self.pre_index]
            root = TreeNode(root_val)

            index = idx_map[root_val]

            self.pre_index += 1

            root.left = helper(in_left, index)
            root.right = helper(index + 1, in_right)

            return root

        idx_map = {val:idx for idx,val in enumerate(inorder)}
        print (idx_map)

        return helper()
