from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        return self.converter(nums, 0, n)

    def converter(self, nums, left, right):
        if left == right:
            return None
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.converter(nums, left, mid)
        node.right = self.converter(nums, mid + 1, right)
        return node


s = Solution()
s.sortedArrayToBST([-10, -3, 0, 5, 9])
s.sortedArrayToBST([1, 3])
