# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import dequeue 
class Solution:
    def isSameTree(self, p, q): 
        if p == None and q == None:
            return True 
        elif p == None or q == None:
            return False 
        elif p.val != q.val:
            return False 
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
