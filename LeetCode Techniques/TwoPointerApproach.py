class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_input = ''

        for char in s:
            if char.isalnum():
                normalized_input += char
              
        normalized_input = normalized_input.lower()
      
        p1 = 0; p2 = len(normalized_input) - 1

        for char in normalized_input:
            if normalized_input[p1] != normalized_input[p2]:
                return False
            else:
                p1 += 1; p2 -= 1

        return True
      
'''
Time: O(N) - the amount of work increases with respect to the size of s
Space: O(N) - normalized_input can be the same size as s
'''
