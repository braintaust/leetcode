import math
class Solution:
    def search_target(self,i,h,nums,target,index):

        #用到进制规则中性质
        #例如在8进制中2和6，((x+6)%8 + 2)%8 = x  （x取1到7）
        #例如在有符号中，最高数字是8，-2和6在2进制显示是一样的
        #(x+6)%8相当于(x-2)
        #计算偏移量            
        f = len(nums)-index
        #计算最小和最大值在有序数组中（未旋转）的下标
        i_f = (i+f)%len(nums)
        h_f = (h+f)%len(nums)
        if i_f > h_f:
            return -1
        #计算中间值，是在有序数组中（未旋转）的下标
        m_b = math.floor((i_f+h_f)/2)
        #返回到旋转之后的下标值
        m = (m_b+index)%len(nums)
        
        if nums[m] > target:
            if m_b-1<0:
                return -1
            return self.search_target(i,m-1,nums,target,index)
        elif nums[m] < target:
            if m_b+1 > len(nums)-1:
                return -1
            return self.search_target(m+1,h,nums,target,index)
        else:
            return m


    def search_min_index(self,i,h,nums,pre):
        m = math.floor((i+h)/2)
        if nums[m]<nums[pre]:
            if nums[m]<nums[m+1] and nums[m]<nums[m-1]:
                return m
            if nums[m]<nums[m+1]:
                return self.search_min_index(i,m-1,nums,m)
        else:
            if m+1>len(nums)-1:
                return 0
            if nums[m]<nums[m+1] and nums[m]<nums[m-1]:
                return m
            if nums[m]<nums[m+1]:
                return self.search_min_index(m+1,h,nums,m)
            if nums[m]>nums[m+1]:
                return m+1

    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        #先找最小值下标
        index= self.search_min_index(0,len(nums)-1,nums,0)
        f = len(nums)-index
        result_index = self.search_target(index,len(nums)-1-f,nums,target,index)

        return result_index

if __name__ == "__main__":
    result = Solution().search([],5)
    print(result)