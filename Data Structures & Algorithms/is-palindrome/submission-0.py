import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ","")
        s="".join(char for char in s if char not in string.punctuation)
        return s==s[::-1]