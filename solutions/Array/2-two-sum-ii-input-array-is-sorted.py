# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Time Complexity - O(n)
# Space Complexity - O(1)
# Hint - Use two pointers in opposite direction, increment left_pt if sum of left_pt + right_pt is less than target, decrement right_pt if sum of left_pt + right_pt is greater than target

    def twoSum_2(self, numbers: List[int], target: int) -> List[int]:

        left_pt = 0
        right_pt = len(numbers) - 1

        while left_pt < right_pt:
            sum = numbers[left_pt] + numbers[right_pt]
            if sum == target:
                return [left_pt + 1, right_pt + 1]
            elif sum < target:
                left_pt += 1
            else:
                right_pt -= 1