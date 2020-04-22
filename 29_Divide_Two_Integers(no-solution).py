class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend<0:
            dividend = -dividend
        if divisor<0:
            divisor = -divisor
        step_len = divisor
        step = 0
        i=0
        while i + step_len < dividend:      
            step+=1
            i= i+ step_len
        return step

if __name__ == "__main__":
    result = Solution().divide(2147483647,1073741823)
    print(result)