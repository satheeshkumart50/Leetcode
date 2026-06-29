    # 41. First Missing Positive
    # https://leetcode.com/problems/first-missing-positive/
    # Time Complexity - O(n) where n is the length of nums
    # Space Complexity - O(1) for the variables used in the algorithm
    # Category - Array
    # Hint - Use the input array to store the presence of numbers in the range [1, n], where n is the length of nums, we can iterate through the array and for each number, if it is in the range [1, n], we can mark its presence by negating the value at its corresponding index, then we can iterate through the array again and find the first index with a positive value, which indicates that the number corresponding to that index is missing, if all indices have negative values, then the missing number is n + 1
    # video - https://www.youtube.com/watch?v=McMC744R3SQ
    def firstMissingPositive(self, nums: List[int]) -> int:

        answer = None
        max_number = len(nums) + 1

        for x, num in enumerate(nums):
            if num <= 0 or num >= max_number:
                nums[x] = max_number

        for y, num in enumerate(nums):
            if num < 0:
                num = -num
            if not num == max_number and num > 0:
                nums[num - 1] = -nums[num - 1]
                if nums[num - 1] > 0:
                    nums[num - 1] = -nums[num - 1]

        for z, num in enumerate(nums):
            if num > 0:
                answer = z + 1
                break

        if not answer:
            return len(nums) + 1

        return answer