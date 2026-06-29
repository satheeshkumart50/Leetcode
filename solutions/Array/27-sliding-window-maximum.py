    # 239. Sliding Window Maximum
    # https://leetcode.com/problems/sliding-window-maximum/
    # Time Complexity - O(n) where n is the length of nums
    # Space Complexity - O(k) where k is the size of the sliding window
    # Category - Array
    # Hint - Use a deque to store the indices of the elements in the sliding window, we can iterate through the array and for each element, we can remove the indices of the elements that are out of the current window from the front of the deque, then we can remove the indices of the elements that are smaller than the current element from the back of the deque, then we can add the index of the current element to the back of the deque, at each step we can add the element at the front of the deque to the result list as it will be the maximum element in the current window
    # video - https://www.youtube.com/watch?v=WcTMo1SHV_s

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # max_idx = []
        # max_idx will always have the index of the maximum element in the current window, here use max_idx as deque not list because we need to pop elements from both ends of the deque, if we use list then popping from the front del max_idx[0] will be O(n) but with deque max_idx.popleft() it will be O(1)
        max_idx = deque()
        result = []
        i = 0

        # Iterate through the first k elements to initialize the deque with the indices of the maximum elements in the first window
        while i < k:
            while max_idx and nums[max_idx[-1]] < nums[i]:
                # del max_idx[-1]
                max_idx.pop()
            max_idx.append(i)
            i += 1

        result.append(nums[max_idx[0]])

        while i < len(nums):

            # comparison of max_idx[0] with i-k is to check if the index at the front of the deque is out of the current window, if it is then we remove it from the deque, because we only want to keep the indices of the elements that are in the current window
            if max_idx[0] <= i - k:
                # del max_idx[0]
                max_idx.popleft()

            while max_idx and nums[max_idx[-1]] <= nums[i]:
                # del max_idx[-1]
                max_idx.pop()
            max_idx.append(i)

            result.append(nums[max_idx[0]])

            i += 1

        return result