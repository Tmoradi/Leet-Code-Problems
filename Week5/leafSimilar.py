# class TreeNode:
#     def __init__(self, x):
#         self.val = x 
#         self.right = None 
#         self.left = None 
    
class Solution:
    def leafSimilar(self,root1,root2):
        # going to need to keep track of the leave values 
        leaves = []
        leaves2 = []
        self.dfs(root1,leaves)
        self.dfs(root2,leaves2)
        return leaves == leaves2 

    def dfs(self,root,leaf):
        if root != None:
            if root.right == None and root.left == None:
                leaf.append(root.val)
            else:
                self.dfs(root.left,leaf)
                self.dfs(root.right,leaf)
