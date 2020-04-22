import math

class Solution:
    def searchPeak(self,i,h,nums):
        if i > h :
           return i
        m = math.floor((i+h)/2)
        if m-1<0 and nums[m] > nums[m+1]:
            return m
        if m+1>len(nums)-1 and nums[m] > nums[m-1]:
            return m
        if nums[m] > nums[m-1] and nums[m] < nums[m+1]:
           return self.searchPeak(m,h,nums)
        if nums[m] < nums[m-1] and nums[m] > nums[m+1]:
           return self.searchPeak(i,m-1,nums)
        if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
           return m
        if nums[m] < nums[m-1] and nums[m] < nums[m+1]:
           return self.searchPeak(m,h,nums)

    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        res = self.searchPeak(0,len(nums)-1,nums)
        return res
if __name__ == "__main__":
    # res = Solution().findPeakElement([1,2,3,1])
    # res = Solution().findPeakElement([1,2,1,3,5,6,4])
    # res = Solution().findPeakElement([7,6,5,4,3,2,1])
    # res = Solution().findPeakElement([1,2,3,4,5,6])
    # res = Solution().findPeakElement([-1,-2,-1,-3])
    # res = Solution().findPeakElement([1,3,2,1,2,1])
    res = Solution().findPeakElement([1,2,1,2,3,1])
    print(res)