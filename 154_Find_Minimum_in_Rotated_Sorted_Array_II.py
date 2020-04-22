import math
class Solution:
    def searchMin(self,i,h,nums):

        ##
        ## 将中轴元素与右边界元素 的解法，但是却并没有说明为什么 可以和 右边界元素 比较得到最终的答案。我自己尝试了用 左边界元素比较 的解法，但是没有解出来。题解区的所有人都是和“右”而不是和“左”边界比较的。所以可能这道题只能讲 将中轴元素与右边界元素比较去解出答案。
        ## 因为找最小值，能够保证的最右侧值固定比最小值要大。如果使用的是左侧值，有可能大，也有可能是最小值，而错过最小值。
        ## 题目要求的是寻找最小值，你跟左边界比较，做 left += 1 ,就可能跳过最小值；如果题目要求是寻找最大值，那么 left += 1可以做，而不是 做 right -= 1来比较右边界元素了
        ## 因为旋转，第一个数据很关键，代表了数组中大数部分和小数部分的分隔线
        if i > h :
            return i
        m = math.floor((i+h)/2)
        ##大数部分
        if nums[m] > nums[h]:
            return self.searchMin(m+1,h,nums)
        ##小数部分
        elif nums[m] < nums[h]:
            return self.searchMin(i,m,nums)
        else: 
            return self.searchMin(i,h-1,nums)

    def findMin(self, nums):
        if(len(nums)==1):
            return nums[0]
        res = self.searchMin(0,len(nums)-1,nums)
        # if res > 0 and res < len(nums)-1:
        #     if nums[res] > nums[res-1]:
        #         return nums[res-1]
        #     if nums[res] > nums[res+1]:
        #         return nums[res+1]
        # if res==0:
        #    if nums[res] > nums[res+1]:
        #        return nums[res+1]
        # if res==len(nums)-1:
        #     if nums[res] > nums[res-1]:
        #         return nums[res-1]
        return nums[res]

if __name__ == "__main__":
    # res = Solution().findMin([10,10,10,10,11])
    # res = Solution().findMin([10,1,10,10,10,10])
    # res = Solution().findMin([10,10,10,10,1])
    # res = Solution().findMin([1,1])
    # res = Solution().findMin([1,2,1])
    res = Solution().findMin([6,2,3,4,5])
    print(res)
    pass