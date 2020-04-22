import math
class Solution:
    def searchBinary(self,i,h,x):
        if i>h:
            return h
        m = math.floor((i+h)/2)
        if(m*m>x):
            return self.searchBinary(i,m-1,x)
        if(m*m<x):
            return self.searchBinary(m+1,h,x) 
        if(m*m==x):
            return m
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        if x < 4:
            return 1
        result = self.searchBinary(0,math.floor(x/2),x)
        return result

if __name__ == "__main__":
    result = Solution().mySqrt(4)
    # result = Solution().mySqrt(20)
    # result = Solution().mySqrt(5)
    print(result)
