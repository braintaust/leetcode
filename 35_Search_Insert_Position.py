# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
import math
class Solution:
    def searchBinary(self,i,h,nums,target):
        if i>h:
            return i
        m = math.floor((i+h)/2)
        if nums[m]>target:
            return self.searchBinary(i,m-1,nums,target)
        if nums[m]<target:
            return self.searchBinary(m+1,h,nums,target)
        if nums[m] == target:
            return m
    def searchInsert(self, nums, target):
        return self.searchBinary(0,len(nums)-1,nums,target)

if __name__ == "__main__":
    result = Solution().searchInsert([1,3,5,6],4)
    print(result)