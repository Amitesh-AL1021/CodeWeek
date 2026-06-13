def remove_dublicates(s):
    str = ""
    for i in s:
        if i not in str:
            str = str + i 
    return str
s = "amitffftesh"
result = remove_dublicates(s)
print(result)