class Solution:
    def isPalindrome(self,s):
        return s==s[::-1]
s="madam"
print(Solution().isPalindrome(s))