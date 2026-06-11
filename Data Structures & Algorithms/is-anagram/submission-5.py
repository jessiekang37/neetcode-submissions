class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        boo = True
        #how to get length of string
        if len(s) != len(t):
            boo = False
        #how to count how many times a char appears in string
        for char in s:
            if s.count(char) != t.count(char):
                boo = False
        return boo
            
