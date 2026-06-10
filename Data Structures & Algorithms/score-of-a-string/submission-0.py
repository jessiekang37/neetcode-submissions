class Solution:
    def scoreOfString(self, s: str) -> int:
        #how to find ASCII: ord()
        #how to parse through a string:
            #method
        #abs value in python: abs(x)
        sum = 0
        for i in range(len(s)-1):
            sum += abs(ord(s[i+1])-ord(s[i]))

        return sum

