def palindrome(s):
    s = s.lower()
    return s == s[::-1]
s = "Aia"
result = palindrome(s)
print(result)