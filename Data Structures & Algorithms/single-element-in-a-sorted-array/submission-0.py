class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        result=0
        for num in nums:
            result^=num
        return result