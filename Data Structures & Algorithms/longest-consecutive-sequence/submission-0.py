class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(set(nums))
        leb=1
        mex=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                mex+=1
            else:
                mex=1
            leb=max(leb,mex)
        return leb