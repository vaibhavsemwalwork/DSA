# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/ 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def levelOrder(self, root):
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qLen= len(q)
            level = [] # will have everything in a level
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res