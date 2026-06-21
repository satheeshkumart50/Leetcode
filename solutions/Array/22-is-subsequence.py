# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/
# Time Complexity - O(n) where n is the length of string t
# Space Complexity - O(1) for the variables used in the algorithm
# Category - Array
# Hint - Use two pointers, one for each string, iterate through the strings and compare characters, if characters match, move the pointer for string s, always move the pointer for string t, at the end if pointer for string s has reached the end, return True else return False
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i,j = 0,0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        if i == len(s):
            return True
        
        return False