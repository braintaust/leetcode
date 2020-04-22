import math 
class Solution:
    def searchMin(self,i,h,nums):
        ## 因为旋转，第一个数据很关键，代表了数组中大数部分和小数部分的分隔线
        if i > h :
            if i == len(nums):
                return nums[0]
            return nums[i]
        m = math.floor((i+h)/2)
        ##大数部分
        if nums[m] >= nums[0]:
            return self.searchMin(m+1,h,nums)
        ##小数部分
        elif nums[m] < nums[0]:
            return self.searchMin(i,m-1,nums)

    def findMin(self, nums):
        if(len(nums)==1):
            return nums[0]
        res = self.searchMin(0,len(nums)-1,nums)
        return res


if __name__ == "__main__":
    # res  = Solution().findMin([3,4,5,0,1,2])
    # res  = Solution().findMin([3,4,5,1,2])
    # res = Solution().findMin([1,2,3,4])
    # res = Solution().findMin([2,1])
    # res = Solution().findMin([1])
    res = Solution().findMin([4,5,1,2,3])

    print(res)
    pass