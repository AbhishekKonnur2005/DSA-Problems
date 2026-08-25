class Solution:
    def isPalindrome(self,head):
        values=[]
        current=head
        while current:
            values.append(current.val)
            current=current.next
        return values==values[::-1]
print(Solution().isPalindrome(head))