# It is a 242 problem in dictionary.

# The first method:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True

# The second method to solve it:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
