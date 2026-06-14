class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        boo = True 
        #remove all spaces
        s=s.replace(" ", "")

        newStr = ''
        for char in s:
            if char.isalnum():
                newStr += char.lower()

        for i in range (len(newStr)//2):
            if newStr[i] != newStr[len(newStr)-i-1]:
                boo = False
        return boo
