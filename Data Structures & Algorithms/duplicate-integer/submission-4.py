class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        letterMap = {}
        for i in range(len(nums)-1):
            n = nums[i]
            letterMap[n] = i
            if nums[i+1] in letterMap:
                return True
        return False
