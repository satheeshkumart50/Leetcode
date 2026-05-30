# DSA Problems Solutions

## Progress
**Solved:** 0/145 problems  
**Last Updated:** May 30, 2026

## Solutions

| # | Problem | Difficulty | LeetCode | Solution | Date Solved | Notes |
|---|---------|-----------|----------|----------|-------------|-------|
| 1 | Two Sum | Easy | [Link](https://leetcode.com/problems/two-sum/) | [Code](https://raw.githubusercontent.com/satheeshkumart50/Leetcode/main/solutions/Array/1-two-sum.py?raw=true) | May 16, 2026 | Use HashMap |
| 167 | Two Sum II - Input Array Is Sorted | Medium | [Link](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Code](https://raw.githubusercontent.com/satheeshkumart50/Leetcode/main/solutions/Array/2-two-sum-ii-input-array-is-sorted.py?raw=true) | May 16, 2026 | Use two pointers in opposite direction, increment first_pt if sum of first_pt + last_pt is less than target; decrement last_pt if sum of first_pt + last_pt is greater than target |
| 26 | Remove Duplicates from Sorted Array | Easy | [Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Code](https://raw.githubusercontent.com/satheeshkumart50/Leetcode/main/solutions/Array/3-remove-duplicates-from-sorted-array.py?raw=true) | May 17, 2026 | Use two pointers in same direction, one pointer to keep track of unique elements and other pointer to iterate through the array, when we find a different element between 1st and 2nd pointer, we move the first pointer and update the value at that pointer with the unique element and incase if not equal then we move second pointer, at the end we return the length of unique elements which is first pointer + 1 |
| 283 | Move Zeroes | Easy | [Link](https://leetcode.com/problems/move-zeroes/) | [Code](https://raw.githubusercontent.com/satheeshkumart50/Leetcode/main/solutions/Array/8-move-zeroes.py?raw=true) | May 17, 2026 | Use two pointers in same direction, If first pointer is 0 and second pointer is not 0, then we move the value at second pointer to first pointer and move both pointers, if first pointer is not 0, then we move both pointers, if first pointer is 0 and second pointer is also 0, then we move only second pointer, at the end we will have all non-zero elements at the beginning of the array and all zeroes at the end of the array |
| 49 | Group Anagrams | Medium | [Link](https://leetcode.com/problems/group-anagrams/) | [Code](https://github.com/satheeshkumart50/Leetcode/tree/810bbc2ca648a3eaeee9c5caf017a5bfef2ab69d/solutions/Array) | May 22, 2026 | - |
| 238 | Product of Array Except Self | Medium | [Link](https://leetcode.com/problems/product-of-array-except-self/) | [Code](https://raw.githubusercontent.com/satheeshkumart50/Leetcode/main/solutions/Array/4-product-of-array-except-self.py?raw=true) | May 23, 2026 | Use two lists to store the product of elements to the left and right of each element after intiating the left_lst[0] = 1 and right_lst[len(nums)-1] = 1, then multiply the corresponding elements of both lists to get the final result, we can optimize space by using the result list to store the product of left and right products, at the end we return the result list |
