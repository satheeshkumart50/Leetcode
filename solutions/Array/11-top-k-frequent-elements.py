# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# Time Complexity - O(n)
# Space Complexity - O(n)
# Category - Array
# Hint - Use a frequency map to store the count of each element in the array, then use a bucket sort algorithm to group elements by their frequency, we can use a list of lists to store the elements with the same frequency, at the end we iterate through the bucket list in reverse order to get the top k frequent elements, important to use extend method to add elements of a list to another list, at the end we return the first k elements of the result list

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_map = dict()
        max_freq = 0

        for x in range(0, len(nums)):
            count_map[nums[x]] = count_map.get(nums[x], 0) + 1
            max_freq = max(max_freq, count_map[nums[x]])

        bucket_lst = [
            [] for _ in range(0, max_freq)
        ]  # important to create empty list of lists

        for (key,v) in count_map.items():  # important to use items() to get key and value
            temp_lst = bucket_lst[v - 1]
            temp_lst.append(key)
            bucket_lst[v - 1] = temp_lst

        result_lst = []

        for y in range(
            len(bucket_lst) - 1, -1, -1
        ):  # important to iterate in reverse order
            result_lst.extend(bucket_lst[y])  # important to use extend to add list elements to another list

        return result_lst[:k]