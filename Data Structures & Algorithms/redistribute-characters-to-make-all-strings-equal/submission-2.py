class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        ans = True
        #take it out of arr form and put into one str:
        string = ""
        
        for word in words:
            string += word
        
        count = Counter(string)
        
        for item in count:
            if count[item] %len(words) !=0:
                ans = False

        return ans