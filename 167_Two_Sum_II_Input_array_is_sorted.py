class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        h = len(numbers) - 1
        while i<h:
            if numbers[i] + numbers[h] > target:
                h = h - 1
            if numbers[i] + numbers[h] < target:
                i = i + 1
            if numbers[i] + numbers[h] == target:
                return [i+1,h+1]
        return [-1,-1]