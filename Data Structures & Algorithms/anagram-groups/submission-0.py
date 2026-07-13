class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use map: order doesn't matter so you can map each word to a list of characters in the words
        
        ans = defaultdict(list) #mapping charCount to list of Anagrams, defaultdict is bc if

        for s in strs:
            #count how many characters it have, stored in an array (a-z, 26 spaces)
            count = [0] * 26 

            for c in s: #map a to index 0 and z to index 25
                count[ord(c) - ord('a')] += 1 #takes ASCII value of current char - ASCII of a, stores the index ex: if it is a, the result index will be 0
                #the +=1 means that everytime this value is countered, that index adds 1 

            ans[tuple(count)].append(s)
        
        #before converting to list, it is just a dictionary view of the list
        return list(ans.values())