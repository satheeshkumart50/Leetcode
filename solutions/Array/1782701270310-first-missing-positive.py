    # 41. First Missing Positive
    # https://leetcode.com/problems/first-missing-positive/
    # Time Complexity - O(n) where n is the length of nums
    # Space Complexity - O(1) for the variables used in the algorithm
    # Category - Array
    # Hint - Use the input array to store the presence of numbers in the range [1, n], where n is the length of nums, we can iterate through the array and for each number, if it is in the range [1, n], we can mark its presence by negating the value at its corresponding index, then we can iterate through the array again and find the first index with a positive value, which indicates that the number corresponding to that index is missing, if all indices have negative values, then the missing number is n + 1
    # video - https://www.youtube.com/watch?v=McMC744R3SQ
    def firstMissingPositive(self, nums: List[int]) -> int:

        # main hint answer will be in the range of 1 <= answer <= len(nums) + 1
        answer = None
        max_number = len(nums) + 1

        # replace all negative numbers and numbers greater than max_number with max_number, because we are only interested in the range [1, n], where n is the length of nums
        for x, num in enumerate(nums):
            if num <= 0 or num >= max_number:
                nums[x] = max_number

        # convert the presence of numbers in the range [1, n] to negative values at their corresponding indices, for example if we have number 3 in the array, we will negate the value at index 2 (3 - 1), if we have number 1 in the array, we will negate the value at index 0 (1 - 1), and so on, if a number is already negative, we will not change it again, this way we can keep track of which numbers are present in the array
        for y, num in enumerate(nums):
            if num < 0:
                num = -num
            if not num == max_number and num > 0:
                nums[num - 1] = -nums[num - 1]
                if nums[num - 1] > 0:
                    nums[num - 1] = -nums[num - 1]

        # find the first index with a positive value, which indicates that the number corresponding to that index is missing, for example if index 0 has a positive value, then number 1 is missing, if index 1 has a positive value, then number 2 is missing, and so on
        for z, num in enumerate(nums):
            if num > 0:
                answer = z + 1
                break

        # if all indices have negative values, then the missing number is n + 1, where n is the length of nums example nums = [1, 2, 3], then answer = 4
        if not answer:
            return len(nums) + 1

        return answer