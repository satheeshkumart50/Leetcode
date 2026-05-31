# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/
# Time Complexity - O(n)
# Space Complexity - O(1)
# Category - Array
# Hint - Use three reverse operations to rotate the array, write a separate function index_rotate(self, nums, start_indx, end_indx) to reverse the array between two indices. first reverse the entire array self.index_rotate(nums, 0, len(nums) - 1), then reverse the first k elements self.index_rotate(nums, 0, k - 1) and then reverse the remaining n-k elements self.index_rotate(nums, 0, k - 1) and when k is greater than the length of the array, we can use k = k % len(nums) to get the effective rotation, at the end we will have the rotated array in place and we return nothing as per the problem statement
# Refer - video - https://www.youtube.com/watch?v=sIzV1SDc-yQ

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        self.index_rotate(nums, 0, len(nums) - 1)
        self.index_rotate(nums, 0, k - 1)
        self.index_rotate(nums, k, len(nums) - 1)

    def index_rotate(self, nums, start_indx, end_indx) -> None:
        while start_indx < end_indx:
            temp_num = nums[end_indx]
            nums[end_indx] = nums[start_indx]
            nums[start_indx] = temp_num
            start_indx += 1
            end_indx -= 1