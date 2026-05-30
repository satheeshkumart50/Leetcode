# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Time Complexity - O(n)
# Space Complexity - O(1)
# Category - Array
# Hint - Use two pointers in opposite direction, one pointer at the beginning of the array and other pointer at the end of the array, calculate the area between the two pointers and update the maximum area, then move the pointer which has smaller height, because moving the pointer with larger height will not increase the area, at the end we return the maximum area

    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        forward_pt = 0
        backward_pt = len(height) - forward_pt - 1

        while forward_pt < backward_pt:
            left_height = height[forward_pt]
            right_height = height[backward_pt]
            current_area = (backward_pt - forward_pt) * min(left_height, right_height)
            max_area = max(max_area, current_area)
            if left_height < right_height:
                forward_pt += 1
            else:
                backward_pt -= 1

        return max_area