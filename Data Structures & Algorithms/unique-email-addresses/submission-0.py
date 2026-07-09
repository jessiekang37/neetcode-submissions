class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:       
        
        #store in a hash set bc it eliminates duplicates 
        unique = set()

        for email in emails:
            #you can split the string using exting "split()" --> here you know it's going to be split into 2 fs
            local, domain = email.split("@")
            #split the first part again and only take the first part before +
            local = local.split("+")[0]
            #this replaces each period with nothing
            local = local.replace(".", "")
            #now that local is all good, you can store them
            unique.add((local, domain))
                    
        #how to get number of unique items: len(set(array)): set() drops all duplicate items len() counts that
        return len(unique)
