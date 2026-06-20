# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Approach 1
        # Time Complexity - O(n*m) where n is the number of strings in the list and m is the average length of the strings
        # Space Complexity - O(1) for the variables used in the algorithm, but O(n) for the input list of strings
        # Category - Array
        # Hint - Use the first string as the prefix and iterate through the rest of the strings in the list, for each string we can compare it with the current prefix and update the prefix to the common characters between the two strings, at the end we return the prefix which will be the longest common prefix among all the strings in the list
        prefix = strs[0]

        for x in range(1, len(strs)):
            temp_prefix = ""
            for y in range(0, len(strs[x])):
                if y < len(prefix) and strs[x][y] == prefix[y]:
                    temp_prefix += strs[x][y]
                else:
                    break
            prefix = temp_prefix

        return prefix

        # Approach 2
        # Time Complexity - O(nlogn.m) due to sorting the list of strings, where n is the number of strings in the list and m is the average length of the strings
        # Space Complexity - O(1) for the variables used in the algorithm, but O(n) for the sorted list of strings
        # Category - Array
        # Hint - Sort the list of strings, then compare the first and last string in the sorted list, we can iterate through the characters of the first and last string and keep adding the common characters to the prefix until we find a mismatch, at the end we return the prefix which will be the longest common prefix among all the strings in the list

        # sorted_strs = sorted(strs)
        # prefix = ""
        # iterate_length = min(len(sorted_strs[0]), len(sorted_strs[-1]))

        # for x in range(0, iterate_length):
        #     if sorted_strs[0][x] == sorted_strs[-1][x]:
        #         prefix += sorted_strs[0][x]
        #     else:
        #         break

        # return prefix