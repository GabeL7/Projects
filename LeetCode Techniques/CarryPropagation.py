class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

'''
Time: O(N) - worst case is to iterate through each digit individually
Space: O(1) - modifying digits in place for a singular variable
'''
