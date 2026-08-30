class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {} #val, index

        for index, val in enumerate(numbers):
            needed = target - val

            if needed in seen:
                return [seen[needed], index + 1]
            else:
                seen[val] = index + 1

        return []