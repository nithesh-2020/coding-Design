class Solution:
    def __init__(self):
        print('output')
    def findPeakElement(self, nums):
        l = 0
        r = len(nums)-1
        while(l < r-1):
            m = l+(r-l)//2
            if nums[m] > nums[m+1] and nums[m] > nums[m-1]:
                return m
            if nums[m] < nums[m+1]:
                l = m+1
            else:
                r = m-1
        return l if nums[l] >= nums[r] else r
s = Solution()
print(s.findPeakElement([1,2,1,3,5,7,3]))
