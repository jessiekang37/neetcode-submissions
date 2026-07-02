class Solution:
    def maxDifference(self, s: str) -> int:
        
        counter = Counter(s)

        oddMax= 0
        evenMin = len(s) #len(s) is the most amount possible

        #extract the values (count) in the counter, and just parse through that
        for count in counter.values():
            #if the count is odd, you compare it to the oddMax
            if count & 1: #this is an optimal way to see if mod instead of mod: odd numbers always end in 1 in computer binary
                oddMax = max(oddMax, count)
            #else, compare it to the min oddMin
            else:
                evenMin = min(evenMin, count)
    
        return oddMax-evenMin

