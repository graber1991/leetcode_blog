# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        max_index= nums.index(max(nums))
        current_max = max(nums)
        return TreeNode(current_max, self.constructMaximumBinaryTree(nums[:max_index]), self.constructMaximumBinaryTree(nums[max_index+1:]))