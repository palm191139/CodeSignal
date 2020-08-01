def checkPalindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

def checkPalindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

def checkPalindrome(s):
    return s == s[::-1]