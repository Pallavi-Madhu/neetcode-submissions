class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       #check if lengths are equal
        if len(s) != len(t) :
            return False

        #define two hash-maps
        hash_s = {}
        hash_t = {}

        #iterate through the string
        for i in s:
            
            #the freq of an element in the hash map hash_s[i] = hash_map.get(element i) and then add 1 to increment the count. .get() will return 0 if element is not present. 
            hash_s[i] = hash_s.get(i,0) + 1
        for i in t:
            hash_t[i] = hash_t.get(i,0) + 1

        # === will return true of same keys and same values in a dict
        return hash_s == hash_t