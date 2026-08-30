class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for index, val in enumerate(nums):
            total = 1

            for index2, val2 in enumerate(nums):
                if index2 != index:
                    total = total * val2

            result.append(total)

        return result
