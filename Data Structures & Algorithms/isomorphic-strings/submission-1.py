class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #forward and backwards maps
        mapST, mapTS = {}, {}

        #parse through each word simultaneously with zip()
        for char1, char2 in zip(s, t):

            #checks if the character is already in the map AND already has another mapped letter
            #checks from the other way around
            if ((char1 in mapST and mapST[char1] != char2) or (char2 in mapTS and mapTS[char2] != char1)):
                return False
            #else, map the character of the index to the character of the index in string two and vice versa
            mapST[char1] = char2
            mapTS[char2] = char1
        return True
