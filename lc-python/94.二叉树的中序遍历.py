#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        # Recursive
        # ans = []
        # self._helper(root, ans)
        # return ans

        # Iterative: use a stack
        ans, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return ans
            node = stack.pop()
            ans.append(node.val)
            root = node.right
    
    def _helper(self, root: 'TreeNode', ans: 'List[int]'):
        if root: 
            self._helper(root.left, ans)
            ans.append(root.val)
            self._helper(root.right, ans)


# @lc code=end

