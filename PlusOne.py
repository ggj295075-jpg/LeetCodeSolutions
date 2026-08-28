class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        m = []
        for i in range(len(digits)):
            degree = 10**i
            num += digits[-1-i]*degree
            i += 1  
        num = str(num+1)
        for i in num:
            m.append(int(i))
        return m
