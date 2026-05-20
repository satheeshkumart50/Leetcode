# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# Time Complexity - O(n)
# Space Complexity - O(1)
# Category - Array
# Hint - Use two pointers in same direction, If first pointer is 0 and second pointer is not 0, then we move the value at second pointer to first pointer and move both pointers, if first pointer is not 0, then we move both pointers, if first pointer is 0 and second pointer is also 0, then we move only second pointer, at the end we will have all non-zero elements at the beginning of the array and all zeroes at the end of the array
# Refer - video - 17-May-2026

    def moveZeroes(self, nums: List[int]) -> None:

        first_pt = 0
        second_pt = 1

        while second_pt < len(nums):
            if nums[first_pt] == 0:
                if nums[second_pt] == 0:
                    second_pt += 1
                else:
                    nums[first_pt] = nums[second_pt]
                    nums[second_pt] = 0
                    second_pt += 1
                    first_pt += 1
            else:
                first_pt += 1
                second_pt += 1