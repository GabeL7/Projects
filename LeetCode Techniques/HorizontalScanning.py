class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        first = strs[0]
        counter = 0

        for i in range(1, len(strs)):
            check = ''

            if len(first) < len(strs[i]):
                counter = len(first)
            else:
                counter = len(strs[i])

            for j in range(0, counter):
                if first[j] != strs[i][j]:
                    break
                check += strs[i][j]
              
            first = check
        return first

'''
S = length of strings
L = length of string comparison
time: O(S*L) - worst case is that all words share a long common prefix 
space: O(L) - check grows with respect to the matching prefix length
'''
