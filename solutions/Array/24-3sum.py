    # 15. 3Sum
    # https://leetcode.com/problems/3sum/
    # Time Complexity - O(n^2) where n is the length of nums
    # Space Complexity - O(1) for the variables used in the algorithm
    # Category - Array
    # Hint - Use two pointers in opposite direction, first sort the array, then iterate through the array and for each element, use two pointers to find the other two elements that sum up to zero, if the sum is less than zero, move the left pointer to the right, if the sum is greater than zero, move the right pointer to the left, if the sum is equal to zero, add the triplet to the result list and move both pointers, at the end we return the result list which will contain all unique triplets that sum up to zero
    # Refer - video - https://www.youtube.com/watch?v=TBePcj8DgxM

    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        result = []

        for i in range(0, len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            first_num = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                second_num = nums[left]
                third_num = nums[right]

                total = first_num + second_num + third_num

                if total == 0:
                    result.append([first_num, second_num, third_num])
                    left += 1
                    right -= 1
                    while left < right and second_num == nums[left]:
                        left += 1
                    while left < right and third_num == nums[right]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result