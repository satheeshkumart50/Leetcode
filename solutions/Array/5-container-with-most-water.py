# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Time Complexity - O(n)
# Space Complexity - O(1)
# Category - Array
# Hint - Use two pointers in opposite direction, one pointer at the beginning of the array and other pointer at the end of the array, calculate the area between the two pointers and update the maximum area, then move the pointer which has smaller height, because moving the pointer with larger height will not increase the area, at the end we return the maximum area

    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        left_pt = 0
        right_pt = len(height) - 1

        while left_pt < right_pt:
            left_height = height[left_pt]
            right_height = height[right_pt]
            current_area = (right_pt - left_pt) * min(left_height, right_height)
            max_area = max(max_area, current_area)
            if left_height < right_height:
                left_pt += 1
            else:
                right_pt -= 1

        return max_area