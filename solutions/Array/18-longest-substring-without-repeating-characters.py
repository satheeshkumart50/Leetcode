# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time Complexity - O(n)
# Space Complexity - O(min(m, n)) where m is the size of the character set
# Category - Array
# Hint - Use a sliding window approach with two pointers and a hash map to store the last seen index of each character, move the second pointer to expand the window and move the first pointer when a repeated character is found and first pointer should be updated to the maximum of its current value and the last seen index of the repeated character plus one, keep track of the maximum length of the substring found so far

    def lengthOfLongestSubstring(self, s: str) -> int:

        freq_map = dict()
        first_pt = 0
        sub_str_max_len = 0

        for second_pt in range(0, len(s)):
            ch = s[second_pt]
            if ch in freq_map:
                first_pt = max(first_pt, freq_map[ch] + 1)

            freq_map[ch] = second_pt
            sub_str_max_len = max(sub_str_max_len, second_pt - first_pt + 1)

        return sub_str_max_len