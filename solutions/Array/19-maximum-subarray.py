# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Time Complexity - O(n)
# Space Complexity - O(1) for the variables used in the algorithm
# Category - Array
# Hint - Use Kadane's Algorithm, we can keep track of the current sum and the maximum sum, we can iterate through the array and for each element we can update the current sum to be the maximum of the current element and the current sum plus the current element, then we can update the maximum sum to be the maximum of the maximum sum and the current sum, at the end we return the maximum sum which will be the largest sum of a contiguous subarray
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = nums[0]
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum