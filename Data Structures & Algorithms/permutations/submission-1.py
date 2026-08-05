class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res,ans=[],[]
        def backtrack():
            if len(ans)==n:
                res.append(ans[:])
                return
            for x in nums:
                if x not in ans:
                    ans.append(x)
                    backtrack()
                    ans.pop()
        backtrack()
        return res