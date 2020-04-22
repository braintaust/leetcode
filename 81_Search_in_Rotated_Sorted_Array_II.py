import math

class Solution:
    ##最坏情况下是O(n)
    def search(self, nums, target):
        if nums is None or len(nums)==0:
            return False
        start = 0
        end = len(nums) - 1
        mid = 0 
        while start <= end:
            mid = start + math.floor((end - start)/2)
            if nums[mid] == target:
                return True
            if nums[start] == nums[mid]:
                start+=1
                continue
            #前半部分有序
            if nums[start] < nums[mid]:
                #target在前半部分
                if nums[mid] > target and nums[start] <= target:
                    end = mid - 1
                else:
                    start = mid + 1
            #后半部分有序
            else:
                #target在后半部分
                if nums[mid] < target and nums[end] >= target:
                    start = mid + 1
                else:
                    end = mid - 1
        return False

        


    # def search(self, nums, target):
    #     # index = self.searchRotatedIndex(0,len(nums)-1,nums,0)
    #     for i in range(0,len(nums)):    
    #         if  target == nums[i]:
    #             return True
    #     return False

if __name__ == "__main__":
    nums = [1,1,1,1,1,1,1,1]
    target = 7
    index = Solution().search(nums,target)
    print(index)