def findMin(nums):
    l, r = 0, len(nums)-1
    while(l<r):
        m = (l+r)//2
        if(nums[m]>nums[l]):
            l = m+1
        else:
            r = m
    return nums[l]
nums = [2,3,0,1]
q = findMin(nums)
print(q)