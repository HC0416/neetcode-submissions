class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurence = {} #char: count
        occurenceB = {}

        for i in s:
            if i in occurence:
                occurence[i] += 1
            else:
                occurence[i] = 1

        for j in t:
            if j in occurenceB:
                occurenceB[j] +=1
            else:
                occurenceB[j] = 1

        for k in occurence:
            if k in occurenceB:
                if occurence[k] != occurenceB[k]:
                    return False
            else:
                return False

        for k in occurenceB:
            if k in occurence:
                if occurence[k] != occurenceB[k]:
                    return False
            else:
                return False
        return True