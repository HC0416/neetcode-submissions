class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        p1 = 0
        p2 = 0

        for i in range(len(nums)):
            t = target - nums[i]
            p1 = i

            for j in range(i+1, len(nums)):
                if nums[j] == t:
                    p2 = j 
                    return[p1, p2]