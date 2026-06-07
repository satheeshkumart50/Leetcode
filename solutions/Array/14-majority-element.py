# 169. Majority Element (Boyer-Moore Voting Algorithm)
# https://leetcode.com/problems/majority-element/
# Time Complexity - O(n)
# Space Complexity - O(1)
# Category - Array
# Hint - Use Boyer-Moore Voting Algorithm, we can keep track of a candidate and a count, this algorithm will just identify if majority element exists or not, it will not give the count of majority element that has to be calculated separately using nums.count(candidate)

    def majorityElement(self, nums: List[int]) -> int:

        candidate = nums[0]
        count = 1

        for x in range(1, len(nums)):
            if nums[x] == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    count = 1
                    candidate = nums[x]

        if (
            nums.count(candidate) > len(nums) // 2
        ):  # this is for test case where there is no majority element, but in this problem we are guaranteed that there is a majority element, arr = [1, 2, 3, 4] or arr = [1, 2, 3, 1, 2, 3]
            return candidate

        return -1