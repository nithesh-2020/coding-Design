class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        r,c  = len(matrix), len(matrix[0])
        l, r = 0, (r*c) - 1
        while(l<=r):
            mid = (l+r)//2
            if(matrix[mid // c][mid % c] > target):
                r = mid-1
            elif (matrix[mid // c][mid % c] < target):
                l = mid+1
            else: return True
        return False