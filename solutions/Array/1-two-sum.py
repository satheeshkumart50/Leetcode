class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

       index_map = dict()
       result_lst = list()

       for x in range(0, len(nums)):
        current_num = nums[x]
        remainder = target - current_num
        
        if remainder in index_map:
            return [index_map.get(remainder), x]
        else:    
            index_map[current_num] = x
        
       return result_lst