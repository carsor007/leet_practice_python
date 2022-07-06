#s -source sequence, p -pattern sequence
def sliding_window_template(s, p):
    #initialize hashmap
    #counter is used to keep track of the number of characters in the pattern, use counter or defaultdict
    counter = Counter(p)

    #two pointers, left and right
    left, right = 0, 0

    #condition checker, update it when trigger some key changes
    #initial value depending on your situation
    count = 0

    #result, return int(such as max or min) or list(such as all the indexes)
    res = 0
    
    #loop through sequence from left to right
    while right < len(s):
        counter[s[right]] += 1

        #update count based on some condition
        if counter[s[right]] > 1:
            count += 1

        # right pointer grows in the outer loop    
        right += 1

        #count condition, the condition may be different
        while count > 0:
            #update the result here if finding minimum

            #increase the left pointer to make it invalid or valid again
            counter[s[left]] -= 1

            #update count based on some condition
            if counter[s[left]] > 0:
                count -= 1

            #left pointer grows in the inner loop
            left += 1

        #update the result here if finding maximum
        res = max(res, right - left)

    return res

    #####################################################################

    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        
        left, right = 0, 0
        count = 0
        res = 0
        
        while right < len(s):
            counter[s[right]] += 1
            
            if counter[s[right]] > 1:
                count += 1
                
            right += 1
            
            while count > 0:
                counter[s[left]] -= 1
                
                if counter[s[left]] > 0:
                    count -= 1
                left += 1
            res = max(res, right - left)
        return res
