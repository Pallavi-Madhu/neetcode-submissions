class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res , r-l+1)
        return res

#logic
#--> i keep a left pointer and a right pointer..iterate through right ptr
#--> if the eleemnt s[r] not in set,then set.add
#--> result = max(result,r-l+1)
#--> if element already in set, then set.remove(s[l]) 
#--> increment l
#--> return result