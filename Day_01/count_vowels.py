def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for i in s.lower():
        if i in vowels:
            count += 1
    return count

s = "amitesh"
result = count_vowels(s)
print(result)