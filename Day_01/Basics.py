# s = "abcdefgh"

# print(s[::2])   # aceg
# print(s[1::2])  # bdfh
# print(s[::-1])  # hgfedcba
# # Here last one is a step calculation by 2 from starting 



def arr(s):
    s = list(set(s))
    s.sort()
    return (s[-2])
s = [1,2,3,4,5,3,9,8,90,70]
print(arr(s))
