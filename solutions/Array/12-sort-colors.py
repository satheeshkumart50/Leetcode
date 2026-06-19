# 75. Sort Colors (Dutch National Flag Algorithm)
# https://leetcode.com/problems/sort-colors/
# Time Complexity - O(n)
# Space Complexity - O(1)
# Category - Array
# Hint - Use Dutch National Flag Algorithm, we can keep track of three pointers, one for the current element, one for the next position of 0 and one for the next position of 2, we can iterate through the array and swap the elements accordingly, if the current element is 0, we swap it with the element at the next position of 0 and move both pointers, if the current element is 1, we just move the current pointer, if the current element is 2, we swap it with the element at the next position of 2 and move the pointer for 2, at the end we will have all 0s at the beginning of the array, followed by all 1s and then all 2s, we return nothing as per the problem statement
    # Refer - video - https://www.youtube.com/watch?v=gaNkjJuXhzI , https://www.youtube.com/watch?v=6sMssUHgaBs

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pt, current_pt = 0, 0
        two_pt = len(nums) - 1

        while current_pt <= two_pt:

            if nums[current_pt] == 0:
                nums[zero_pt], nums[current_pt] = nums[current_pt], nums[zero_pt]
                current_pt += 1
                zero_pt += 1
            elif nums[current_pt] == 1:
                current_pt += 1
            else:
                nums[current_pt], nums[two_pt] = nums[two_pt], nums[current_pt]
                two_pt -= 1