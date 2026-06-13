# def Check_angram(s1,s2):
#     return sorted(s1.lower()) == sorted(s2.lower())
# print(Check_angram("Amitesh","Amitesh"))
# print(Check_angram("Amitesh","Thakur"))

def check_angram(s1,s2):
    s1 = s1.casefold()
    s2 = s2.casefold()
    return sorted(s1) == sorted(s2)
print(check_angram("Amit","Amit"))
print(check_angram("Ram","Kam"))