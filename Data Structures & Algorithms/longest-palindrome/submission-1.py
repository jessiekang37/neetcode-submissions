class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        hasOdd = 0

        #count how many times each letter appears
        count = Counter(s)

        for item in count:

            if count[item] %2 == 0:
                ans += count[item]
            else:
                ans += count[item] -1
                hasOdd = 1
        
        return ans + hasOdd


        
