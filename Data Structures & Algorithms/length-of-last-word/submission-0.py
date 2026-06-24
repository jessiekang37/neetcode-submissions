class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #make a var for the length
        i = len(s)-1
        length = 0
        #how to prevent the fact that end might be space?using a while loop to make sure that if the current char is a space, it keeps counting down
        while s[i] == ' ':
            i-=1
        #ok now no longer space, while we are still in range and the char is NOT a space
        while i >= 0 and s[i] != ' ':
            length +=1
            i-=1

        return length



        
