import math
class Solution:
    def searchMinI(self,i,h,nums,target,min_index):
        if i > h:
           return min_index
        m = math.floor((i+h)/2)
        if nums[m] == target:
            if m <= min_index:
                min_index = m
            return self.searchMinI(i,m-1,nums,target,min_index)
        if nums[m] < target:
            return self.searchMinI(m+1,h,nums,target,min_index)
            
    def searchMaxI(self,i,h,nums,target,max_index):
        if i > h:
           return max_index
        m = math.floor((i+h)/2)
        if nums[m] == target:
            if m >= max_index:
                max_index = m
            return self.searchMaxI(m+1,h,nums,target,max_index)
        if nums[m] > target:
            return self.searchMaxI(i,m-1,nums,target,max_index)

    def searchTravls(self,i,h,nums,target):  
        if i>h:
            return [-1,-1]
        m = math.floor((i+h)/2)
        if nums[m]<target:
            return self.searchTravls(m+1,h,nums,target)
        if nums[m]>target:
            return self.searchTravls(i,m-1,nums,target)
        if nums[m]==target:
            relist = [] 
            relist.append(self.searchMinI(i,m-1,nums,target,m))
            relist.append(self.searchMaxI(m+1,h,nums,target,m))
            return relist
    
    def searchRange(self, nums, target):
        result_list = self.searchTravls(0,len(nums)-1,nums,target)
        print (result_list)
        
        return result_list


if __name__ == "__main__":
    # Solution().searchRange([5,7,7,8,8,8,8,8,8,8,8,10],8)
    Solution().searchRange([8,8,8,8,8,8,8,8,8,8,8,8],6)

    