class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        #Counter() maps item in arr to its number of appearences - use in python!
        count = Counter(arr)

        for item in count:
            if count[item] == 1:
                k-=1
                if k == 0:
                    return item
        return ""