# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0  # Counter of max diameter

        def dfs(root):  # Create DFS recursive function
            nonlocal res  # Indicate that res is variable which be in external function

            if not root:  # Check of null
                return 0
            left = dfs(root.left)  # Recursive for left subTree
            right = dfs(root.right)  # Recursive for right subTree
            res = max(res, left + right)  # Check which a variable biggest

            return 1 + max(left, right)  # Return len of this subTree

        dfs(root)  # Use DFS for "root"
        return res
