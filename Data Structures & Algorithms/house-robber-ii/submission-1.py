class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2: return max(nums)
        first=nums[:-1]
        last=nums[1:]
        dp1=[0]*len(first)
        dp2=[0]*len(last)
        dp1[0]=nums[0]
        # iterate through the first list
        for i in range(1,len(first)):
            dp1[i]=max(dp1[i-1],dp1[i-2]+first[i])
        dp2[0]=last[0]
        for i in range(1,len(last)):
            dp2[i]=max(dp2[i-1],dp2[i-2]+last[i])
        return max(dp1[-1],dp2[-1])

