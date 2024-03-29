# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]


# Time Complexity: O(log N), where N is the number of nodes.
# Space Complexity: O(H) to keep the recursion stack, where
# H is the height of the tree, H = log N for balanced tree


# Algorithm
#
# If key > root.val then delete the node to delete is in the right subtree root.right = deleteNode(root.right, key).
#
# If key < root.val then delete the node to delete is in the left subtree root.left = deleteNode(root.left, key).
#
# If key == root.val then the node to delete is right here. Let's do it :
#
# If the node is a leaf, the delete process is straightforward : root = null.
#
# If the node is not a leaf and has the right child, then replace the node value by a successor value root.val = successor.val, and then recursively delete the successor in the right subtree root.right = deleteNode(root.right, root.val).
#
# If the node is not a leaf and has only the left child, then replace the node value by a predecessor value root.val = predecessor.val, and then recursively delete the predecessor in the left subtree root.left = deleteNode(root.left, root.val).
#
# Return root.


# class Solution:
#     def successor(self, root):
#         root = root.right
#         while root.left:
#             root = root.left
#         return root.val
#
#     def predecessor(self, root):
#         root = root.left
#         while root.right:
#             root = root.right
#         return root.val
#
#     def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
#         if not root:
#             return None
#
#         if key > root.val:
#             root.right = self.deleteNode(root.right, key)
#
#         elif key < root.val:
#             root.left = self.deleteNode(root.left, key)
#
#         else:
#             if not root.left and not root.right:
#                 root = None
#
#             elif root.right:
#                 root.val = self.successor(root)
#                 root.right = self.deleteNode(root.right, root.val)
#             else:
#                 root.val = self.predecessor(root)
#                 root.left = self.deleteNode(root.left, root.val)
#
#         return root

class Solution:
    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root
