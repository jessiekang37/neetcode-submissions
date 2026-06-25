class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            maxNum = -1 #value for the last position - keeps a running max
            
            for j in range(i+1, len(arr)):
                #using the max() function to get the maximum from the right side of i, then set i to that after the j loop is over
                maxNum = max(maxNum, arr[j])
            arr[i] = maxNum
    
        
        return arr