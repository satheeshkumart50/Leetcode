# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# Time Complexity - O(n)
# Space Complexity - O(n)
# Category - Array
# Hint - Use two arrays to store the maximum height to the left and right of each element, then calculate the water trapped at each element using formula min(left_max, right_max) - height[i], if the result is positive then we add it to the total water trapped, at the end we return the total water trapped, we can optimize space by using the input array to store the maximum height to the left and right of each element, at the end we return the total water trapped
# Refer - video - https://www.youtube.com/watch?v=09KF1hjWoSU (Nikhil Video is best for this problem)

    def trap(self, height: List[int]) -> int:

        left_max_lst = [0] * len(height)
        right_max_lst = [0] * len(height)
        max_ht = height[0]
        total_unit = 0

        for x in range(1, len(height)):
            max_ht = max(max_ht, height[x - 1])
            left_max_lst[x] = max_ht

        max_ht = height[len(height) - 1]

        for x in range(len(height) - 2, -1, -1):
            max_ht = max(max_ht, height[x + 1])
            right_max_lst[x] = max_ht

        for x in range(0, len(height)):
            temp_unit = min(left_max_lst[x], right_max_lst[x]) - height[x]

            if temp_unit > 0:
                total_unit += temp_unit

        return total_unit