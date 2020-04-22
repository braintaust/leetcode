import math
class Solution:
    def caluPow(self,x,n):
        if n==1:
            return x
        if n==0:
            return 1
        l = math.floor(n/2)
        r = n-l
        if (r >= l):
           devia = self.caluPow(x,r-l)
        else:
            devia = self.caluPow(x,l-r)
        re = self.caluPow(x,l)
        return re * re * devia
        
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return x
        if n==0:
            return 1
        if n<0 and x!=0:
            x=1/x
            n=(-1)*n
        return self.caluPow(x,n)

if __name__ == "__main__":
    # result = Solution().myPow(2.1000,3)
    # result = Solution().myPow(0.44528,0)
    # result = Solution().myPow(0.00001,2147483647)
    result = Solution().myPow(2.000,10)
    print(result)
        
