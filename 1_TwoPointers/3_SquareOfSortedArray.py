#Leetcode: 977 Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        j=len(nums)-1
        i=0
        res=[0]*len(nums)
        k=len(res)-1
        while j>=i:
            if(nums[i]**2 <nums[j]**2):
                res[k]=nums[j]**2
                j-=1
            else:
                res[k]=nums[i]**2
                i+=1
            k-=1
        
        return res