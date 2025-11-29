# 2 ways: sort + 2 pointers on a sorted copy of the array with original indices, hashmap one pass

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hmap:
                return [i,hmap[diff]]
            else:
                hmap[nums[i]] = i
        
        
            

        