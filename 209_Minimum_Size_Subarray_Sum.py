class Solution:
    def minSubArrayLen(self, s, nums):
        if (len(nums)==0):
            return 0
        i,j = 0, 0
        cnt = 1
        min = len(nums)+1
        sum = nums[i]
        while i < len(nums) :
            if (sum >= s):
                if(min >= cnt):
                    min = cnt
                sum = sum - nums[i]
                cnt = cnt - 1
                i = i + 1  
            else:
                cnt = cnt + 1
                j = j + 1
                if j > len(nums)-1:
                    break
                sum = sum + nums[j]
        if min == len(nums)+1:
            return 0
        else:
            return min
                

if __name__ == "__main__":
    # res = Solution().minSubArrayLen(s = 12, nums = [1,3,1,2,4,1])
    # res = Solution().minSubArrayLen(s = 100, nums = [])
    res = Solution().minSubArrayLen(s = 3, nums = [1,1])
    print(res)