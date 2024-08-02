class Solution:
    def __init__(self):
        print("output")
        #self.nums=nums
        #self.target=nums

    def searchRange(self, nums, target):
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]

    def binSearch(self, nums, target, leftbias):
        l,r = 0, len(nums) - 1
        i = -1
        while l<=r:
            m = (l+r)//2
            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
            else:
                i = m
                if leftbias:
                    r = m-1
                else:
                    l =m+1
        return i


#search = Solution()
#q = search.searchRange([1,1,2,2,2,3,4,4,4,5], 4)
s=Solution()
print(s.searchRange([1,1,2,2,2,3,4,4,4,5],4))




