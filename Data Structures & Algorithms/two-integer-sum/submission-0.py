class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #val, index

        for index, val in enumerate(nums):
            valueNeeded = target - val

            if valueNeeded in seen:
                return[seen[valueNeeded], index]
            else:
                seen[val] = index
        
        return []
