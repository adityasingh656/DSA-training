#Leetcode: 1. Two Sum 1
class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i









#leetcode: 167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i=0
        j=len(numbers)-1
        while (i+j!=target or i<j):
            ans=numbers[i]+numbers[j]
            if(ans<target):
                i+=1
            elif(ans>target):
                j-=1
            else:
                return [i+1,j+1]
        return [-1,-1]