class Solution:
    def maxDifference(self, s: str) -> int:
        
        counter = Counter(s)

        odd = []

        even = []

        for char in s:
            #make an array of odd
            if counter[char]%2 == 1:
                odd.append(counter[char])
            #make an array of even
            else:
                even.append(counter[char])
        
        diff = (max(odd) - min(even))

        return diff

