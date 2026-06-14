class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            #add letter into array
            arr.append(nums[i])
        for j in range(len(nums)):
            arr.append(nums[j])
        return arr
        