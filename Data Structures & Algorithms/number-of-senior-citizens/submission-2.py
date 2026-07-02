class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
                #if int((details[i])[11]) > 6 or (int((details[i])[11]) == 6 and int((details[i])[12])> 0 ):
                #make substring instead
                if int((details[i])[11:13]) > 60 :
                    count +=1
        return count