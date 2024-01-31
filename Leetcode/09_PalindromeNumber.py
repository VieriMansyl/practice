class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0): return False
        stringX = str(x)
        for i in range(len(stringX) // 2):
            if stringX[i] != stringX[len(stringX) - i -1]:
                return False
        return True