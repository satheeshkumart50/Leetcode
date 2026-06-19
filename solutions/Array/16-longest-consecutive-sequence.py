# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
# Time Complexity - O(n)
# Space Complexity - O(n)
# Category - Array
# Hint - Use a set to store the unique elements of the array, then iterate through the set and for each element, check if it is the start of a sequence (i.e. if num-1 is not in the set), if it is the start of a sequence, then we can keep checking for the next elements in the sequence (i.e. num+1, num+2, etc.) until we find an element that is not in the set, we can keep track of the length of the current sequence and update the maximum length at the end, at the end we return the maximum length of the consecutive sequence
# https://www.youtube.com/watch?v=gHyzQiFu4xY

    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        seq_len = 0 if not nums else 1

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            else:
                temp_seq_len = 1
                next_num = num + 1
                while next_num in nums_set:
                    temp_seq_len += 1
                    next_num += 1
                seq_len = max(temp_seq_len, seq_len)

        return seq_len