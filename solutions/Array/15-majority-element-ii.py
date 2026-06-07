# 229. Majority Element II (Boyer-Moore Voting Algorithm)
# https://leetcode.com/problems/majority-element-ii/
# Time Complexity - O(n)
# Space Complexity - O(1)
# Category - Array
# Hint - Use Boyer-Moore Voting Algorithm, we can keep track of two candidates and their counts, this algorithm will just identify if majority elements exists or not, it will not give the count of majority elements that has to be calculated separately using nums.count(candidate)

    def majorityElement(self, nums: List[int]) -> List[int]:

        candidate1 = None
        candidate2 = None
        vote1 = 0
        vote2 = 0

        # Phase 1: Find majority candidates
        for x in nums:
            if candidate1 == x:
                vote1 += 1
            elif candidate2 == x:
                vote2 += 1
            elif vote1 == 0:
                candidate1 = x
                vote1 = 1
            elif vote2 == 0:
                candidate2 = x
                vote2 = 1
            else:
                vote1 -= 1
                vote2 -= 1

        # Phase 2: Verify if majority candidates count is greater than n/3
        result = []
        for c in (candidate1, candidate2):
            if c is not None and nums.count(c) > len(nums) // 3:
                result.append(c)

        return result