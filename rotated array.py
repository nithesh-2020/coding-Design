class solution:
    def search(self, arr, target):
        if (len(arr) == 0): return -1

        l, r = 0, len(arr)-1
        #finding pivot
        while(l < r):
            mid = (l + r) // 2
            if (arr[mid] > arr[r]):
                l = mid+1
            else:
                r = mid

        strt = l
        l = 0
        r = len(arr)-1

        #finding position of target
        if(target >= arr[strt] and target <= arr[r]):
            l = strt
        else:
            r = strt

        #Basic Binary search

        while(l <= r):
            mid = (l + r) // 2
            if (arr[mid] == target):
                return mid
            elif ( arr[mid] < target ):
                l = mid-1
            else:
                r = mid-1

        return -1
q = solution()
q = q.search([3,4,5,0,1,2], 1)
print(q)