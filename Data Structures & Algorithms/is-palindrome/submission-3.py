class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        lastPointer =n - 1
        firstPointer = 0
        while firstPointer < lastPointer:
            while firstPointer < lastPointer and not s[firstPointer].isalnum():
                    firstPointer +=1
            
            while firstPointer < lastPointer and not s[lastPointer].isalnum():
                    lastPointer -=1

            if s[firstPointer].lower() != s[lastPointer].lower():
                print(s[firstPointer])
                print(s[lastPointer])
                return False
            else:
                firstPointer +=1
                lastPointer -=1

        
        return True