class Solution(object):
    def findKthLargest(self, nums, k):
        nums = sorted(nums)
        if len(nums)==1 and k==1:
            return nums[0]
        return nums[len(nums)-k]