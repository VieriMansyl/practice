class Solution:
    def romanToInt(self, s: str) -> int:
        arr = [0 for i in range(len(s))]
        currNum = 0 ; futNum = 0 ; i = 0
        sum = 0
        while i < len(s):
            currNum = self.converter(s[i])
            if(i != len(s)-1):
                futNum = self.converter(s[i+1])
                if currNum < futNum:
                    sum += futNum-currNum
                    i += 1
                else:
                    sum += currNum
            else:
                sum += currNum
            i+=1
        return sum
    
    
    def converter(self, st : str) -> int:
        if st == 'I': return 1
        if st == 'V': return 5
        if st == 'X': return 10
        if st == 'L': return 50
        if st == 'C': return 100
        if st == 'D': return 500
        if st == 'M': return 1000