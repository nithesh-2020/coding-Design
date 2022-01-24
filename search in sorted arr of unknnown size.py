def search(arr, target):
        l = 0
        r = 1
        while (arr[r] < target and arrayReader.get(r)!=14789900):
            l = r
            r = 2*r
        while(l<=r):

            mid = l+(r-l)//2
            if (target == arr[mid]):
                return mid
            if(target>arr[mid]):
                l = mid+1
            else:
                r = mid-1
        return -1
arr = [0,1,2,5,6]
print(search(arr,7))



