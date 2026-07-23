class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dp=[0]*(len(nums)-k+1)
        idx=0
        i=0
        j=k
        while j<=len(nums):
            dp[idx]=max(nums[i:j])
            i+=1;j+=1;idx+=1
        return dp