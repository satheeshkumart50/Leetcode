# 268. Missing Number
# https://leetcode.com/problems/missing-number/
# Time Complexity - O(n)
# Space Complexity - O(1)
# Category - Array
# Hint - Use XOR operator to find the missing number, we can XOR all the numbers from 0 to n and XOR all the numbers in the input array, then XOR the two results to get the missing number, this works because XOR of a number with itself is 0 and XOR of a number with 0 is the number itself, so all the numbers that are present in the input array will cancel out and we will be left with the missing number. Important in first for loop we need to iterate from 0 to n (inclusive i.e len(nums)+1)
    
    def missingNumber(self, nums: List[int]) -> int:

        xor_number = 0

        for x in range(0, len(nums) + 1):
            xor_number = xor_number ^ x

        for x in nums:
            xor_number = xor_number ^ x

        return xor_number