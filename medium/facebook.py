class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                temp = ''
                while stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                    
                stack.append(int(k) * temp)
        return ''.join(stack)

########################################################

def checkPossibility(self, nums: List[int]) -> bool:
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            count += 1
            if i == 0:
                nums[i] = nums[i + 1]
            elif nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i - 1]
            else:
                nums[i + 1] = nums[i]
        if count > 1:
            return False
    return True

    ########################################################
    #Input: s = "lee(t(c)o)de)"
    #Output: "lee(t(c)o)de"
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        # Looping throught the string
        for c in s:
            # Possible chars in string are "(" or ")" or lowercase english letter
            # If current char is ")"
            if c == ")":
                string = ""
                # We pop the top element from stack and concatenate value to string
                # till stack becomes empty or we find "("
                while stack and stack[-1] != "(":
                    string = stack.pop() + string
                # If stack is not empty, that means we break out of loop since we found
                # "(" at top of stack.
                # So, we pop "(" from stack and add "(" + string + ")"
                if stack: 
                    stack.pop()
                    stack.append("(" + string + ")")
                # If stack is empty, that means we haven't found a "(" for the
                # current ")". So we just append string to stack
                else: stack.append(string)
            # If char is "(" or alphabet we add it stack
            else: stack.append(c)
        
        validString = ""
        # Looping through the stack to concatenate all the vals in the stack to
        # generate resultant string
        for string in stack:
            # If string is "(" that means it has not supporting ")" in the given
            # string, so we don't add it to our result
            if string != "(": validString += string
        # Returning the string
        return validString

        ########################################################
class Solution:
    def minDeletions(self, s: str) -> int:
        ans = 0
        setS = set(s)
        arr = []
    
        for i in setS:
            print(i)
            cnt = s.count(i)
            while cnt in arr and cnt > 0:
                 cnt -= 1
                 ans += 1
            else:
                arr.append(cnt)
        return ans

########################################################

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a dictionary to store the index of each character in the order string
        # For example, if order = "abc", then the dictionary will be {"a": 0, "b": 1, "c": 2}
        # We can use this dictionary to compare the index of two characters in the words
        # For example, if the first character in the first word is "a" and the first character
        # in the second word is "b", then the first word is alphabetically before the second
        # word.
        dict = {}
        for i in range(len(order)):
            dict[order[i]] = i
        # Loop through the words
        for i in range(len(words) - 1):
            # If the first character in the current word is alphabetically before the first
            # character in the next word, then the words are not sorted.
            if dict[words[i][0]] > dict[words[i + 1][0]]:
                return False
            # If the first character in the current word is alphabetically before the first
            # character in the next word, then the words are not sorted.
            if len(words[i]) > len(words[i + 1]):
                return False
            # If the first character in the current word is alphabetically before the first
            # character in the next word, then the words are not sorted.
            if len(words[i]) < len(words[i + 1]):
                return False
            # If the first character in the current word is alphabetically before the first
            # character in the next word, then the words are not sorted.
            if words[i] > words[i + 1]:
                return False
        return True

        ########################################################


#Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
#Output: true
#Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
#
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a dictionary to store the index of each character in the order string
        # For example, if order = "abc", then the dictionary will be {"a": 0, "b": 1, "c": 2}
        # We can use this dictionary to compare the index of two characters in the words
        # For example, if the first character in the first word is "a" and the first character
        # in the second word is "b", then the first word is alphabetically before the second
        # word.
        dict = {}
        for i in range(len(order)):
            dict[order[i]] = i
        # Loop through the words
        for i in range(len(words) - 1):
            # If the first character in the current word is alphabetically before the first
            # character in the next word, then the words are not sorted.
            if dict[words[i][0]] > dict[words[i + 1][0]]:
                return False
            # If the first character in the current word is alphabetically before the first
            # character in the next word, then the words are not sorted.
            if len(words[i]) > len(words[i + 1]):
                return False
            # If the first character in the current word is alphabetically before the first
            # character in the next word, then the words are not sorted.
            if len(words[i]) < len(words[i + 1]):
                return False
            # If the first character in the current word is alphabetically before the first
            # character in the next word, then the words are not sorted.
            if words[i] > words[i + 1]:
                return False
        return True

########################################################
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # If the string is empty or has only one character, it is a valid palindrome
        if len(s) <= 1:
            return True
        # If the string is not a palindrome, then we return false
        if s != s[::-1]:
            return False
        # If the string is a palindrome, then we check if it is a valid palindrome
        # by checking if it is a valid palindrome without the first and last character
        # If it is a valid palindrome, then we return true
        # If it is not a valid palindrome, then we return false
        return (s[1:-1])

########################################################


# given a k sorted lists of size n each, merge them into one sorted list
# example:
# [
#   [1,3,5,7],
#   [2,4,6,8],
#   [0,9,10,11]
# ]
# output: [0,1,2,3,4,5,6,7,8,9,10,11]
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    # create a dummy node
    dummy = ListNode(0)
    # create a pointer to the last node of the dummy node
    curr = dummy
    # create a queue to store the nodes of each list
    queue = []
    # loop through the lists
    for list in lists:
        # if the list is not empty, add it to the queue
        if list:
            queue.append(list)
    # while the queue is not empty
    while queue:
        # sort the queue by the value of the node
        queue.sort(key=lambda x: x.val)
        # get the first node in the queue
        node = queue.pop(0)
        # if the node is not None
        if node:
            # add the node to the dummy node
            curr.next = node
            # set the current node to the next node
            curr = curr.next
            # if the next node is not None
            if node.next:
                # add the next node to the queue
                queue.append(node.next)
    # return the dummy node
    return dummy.next

# check if word is almost a palindrome
def isPalindrome(self, word: str) -> bool:
    # if the length of the word is less than 2, it is a palindrome
    if len(word) < 2:
        return True
    # if the length of the word is more than 2, it is not a palindrome
    if len(word) > 2:
        return False
    # if the first and last characters are the same
    if word[0] == word[-1]:
        # return true
        return True
    # if the first and last characters are not the same
    else:
        # return false
        return Falsesp