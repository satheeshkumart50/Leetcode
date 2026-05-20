# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Time Complexity - O(n)
# Space Complexity - O(1)
# Category - Array
# Hint - Use two lists to store the product of elements to the left and right of each element after intiating the left_lst[0] = 1 and right_lst[len(nums)-1] = 1, then multiply the corresponding elements of both lists to get the final result, we can optimize space by using the result list to store the product of left and right products, at the end we return the result list
# Refer - video - https://www.youtube.com/watch?v=G9zKmhybKBM

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_lst = [None] * len(nums)
        right_lst = [None] * len(nums)
        result_lst = [None] * len(nums)

        left_lst[0] = 1
        right_lst[len(nums) - 1] = 1

        for x in range(1, len(nums)):
            left_lst[x] = left_lst[x - 1] * nums[x - 1]

        for y in range(len(nums) - 2, -1, -1):
            right_lst[y] = right_lst[y + 1] * nums[y + 1]

        for z in range(0, len(nums)):
            result_lst[z] = left_lst[z] * right_lst[z]

        return result_lst
