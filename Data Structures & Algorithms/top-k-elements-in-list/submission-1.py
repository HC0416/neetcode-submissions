class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {} #value : count
        freElement = []
        frequentKey = 0

        for i in nums:
            if i in occurences:
                occurences[i] += 1
            else:
                occurences[i] = 1

        for j in range(k):
            frequentValue = 0
            for key, value in occurences.items():
                if value > frequentValue:
                    frequentValue = value
                    frequentKey = key
                    
            freElement.append(frequentKey)
            occurences.pop(frequentKey)

        return freElement

        