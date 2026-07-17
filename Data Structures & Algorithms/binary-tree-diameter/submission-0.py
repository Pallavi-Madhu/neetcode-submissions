# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if root == None:
        #     return 0
        # return max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        self.res = 0
        def depth(curr):
            if curr == None:
                return 0
            left = depth(curr.left)
            right = depth(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left,right)
        depth(root)
        return self.res