class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)/2
        majority = 0

        counter = Counter(nums)

        for item in counter:
            if counter[item] > size:
                majority = item

        return majority