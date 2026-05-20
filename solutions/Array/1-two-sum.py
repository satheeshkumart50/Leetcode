# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Time Complexity - O(n)
# Space Complexity - O(1)
# Category - Array
# Hint - Use HashMap

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_map = dict()

        for x in range(0, len(nums)):
            remainder = target - nums[x]
            if remainder in index_map:
                return [index_map[remainder], x]
            else:
                index_map[nums[x]] = x