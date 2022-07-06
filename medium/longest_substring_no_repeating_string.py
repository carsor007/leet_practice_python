#Sliding window using a set
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
            res = max(res, r - l + 1)
        return res


        #Sliding window using a dictionary

        class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strHash = {}
        l = 0
        res = 0
        
        for c in range(len(s)):
            if s[c] in strHash:
                l = max(l, (strHash[s[c]] + 1))
            res = max(res, (c - l + 1))
            strHash[s[c]] = c     
        return res