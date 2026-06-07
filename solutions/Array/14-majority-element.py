# 169. Majority Element (Boyer-Moore Voting Algorithm)
# https://leetcode.com/problems/majority-element/
# Time Complexity - O(n)
# Space Complexity - O(1)
# Category - Array
# Hint - Use Boyer-Moore Voting Algorithm, we can keep track of a candidate and a count, we iterate through the array and if the current element is the same as the candidate, we increment the count, if it is different, we decrement the count, if the count becomes 0, we update the candidate to the current element and reset the count to 1, at the end we return the candidate, we can add an additional check to verify if the candidate is actually the majority element by counting its occurrences in the array and comparing it to n/2, but in this problem we are guaranteed that there is a majority element so this check is not necessary

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