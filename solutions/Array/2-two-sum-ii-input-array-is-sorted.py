# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Time Complexity - O(n)
# Space Complexity - O(1)
# Hint - Use two pointers in opposite direction, increment first_pt if sum of first_pt + last_pt is less than target, decrement last_pt if sum of first_pt + last_pt is greater than target

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        first_pt = 0
        last_pt = len(numbers)-1

        while first_pt < last_pt:
            sum = numbers[first_pt]+numbers[last_pt]
            if sum == target:
                return [first_pt+1, last_pt+1]
            elif sum < target:
                first_pt += 1
            else:
                last_pt -= 1