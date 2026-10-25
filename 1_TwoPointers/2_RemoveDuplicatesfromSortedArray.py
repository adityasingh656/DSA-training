#leetcode: 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k=1
        i,j=0,1
        while(j<len(nums)):
            if nums[j]!=nums[j-1]:
                nums[i+1]=nums[j]
                i,j,k=i+1,j+1,k+1
            else:
                j+=1
        return k


#leetcode: 80. Remove Duplicates from Sorted Array II
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k=1
        i=0
        c=1
        for j in range(1,len(nums)):
            if(nums[j]==nums[j-1] and c<2):
                nums[i+1]=nums[j]
                c+=1
                i+=1
                k+=1
            elif(nums[j]==nums[j-1] and c>=2):
                c+=1
            else:
                nums[i+1]=nums[j]
                c=1
                i+=1
                k+=1
        return k

        