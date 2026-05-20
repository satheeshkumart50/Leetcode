# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array
# Time Complexity - O(n)
# Space Complexity - O(1)
# Hint - Use two pointers in same direction, one pointer to keep track of unique elements and other pointer to iterate through the array, when we find a different element between 1st and 2nd pointer, we move the first pointer and update the value at that pointer with the unique element and incase if not equal then we move second pointer, at the end we return the length of unique elements which is first pointer + 1
# Refer - video - 17-May-2026

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        first_pt = 0
        second_pt = 1

        while second_pt < len(nums):

            if nums[first_pt] == nums[second_pt]:
                second_pt += 1
            else:
                first_pt += 1
                nums[first_pt] = nums[second_pt]

        return first_pt+1