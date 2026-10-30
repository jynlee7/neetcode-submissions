# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # I should recursively check whether the left is less than root
        # and right is greater than root
        # if all pass return true
        # else return false
        if not root:
            return False
        if not root.left:
            pass
        elif root.left.val < root.val:
            return self.isValidBST(root.left)
        else:
            return False
        if not root.right:
            pass
        elif root.right.val > root.val:
            return self.isValidBST(root.right)
        else:
            return False
        return True