import math
class Solution:
    def searchBinaryRow(self,i,h,row,target):
        if i > h :
            return h
        m = math.floor((i+h)/2)
        if row[m][0] > target:
            return self.searchBinaryRow(i,m-1,row,target)
        if row[m][0] < target:
            return self.searchBinaryRow(m+1,h,row,target)
        if row[m][0] == target:
            return m
    def searchBinaryCol(self,i,h,col,target):
        if i > h :
            return -1
        m = math.floor((i+h)/2)
        if col[m] > target:
            return self.searchBinaryCol(i,m-1,col,target)
        if col[m] < target:
            return self.searchBinaryCol(m+1,h,col,target)
        if col[m] == target:
            return m
    def searchMatrix(self, matrix, target):
        index = self.searchBinaryRow(0,len(matrix)-1,matrix,target)
        result = self.searchBinaryCol(0,len(matrix[index])-1,matrix[index],target)
        if result > -1:
            return True
        else:
            return False

if __name__ == "__main__":
    # matrix = [
    # [1,   3,  5,  7],
    # [10, 11, 16, 20],
    # [23, 30, 34, 50]
    # ]
    # target = 8
    matrix = [[1]]
    target = 1   
    result = Solution().searchMatrix(matrix,target)
    print(result)