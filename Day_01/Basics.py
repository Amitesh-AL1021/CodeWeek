# # s = "abcdefgh"

# # print(s[::2])   # aceg
# # print(s[1::2])  # bdfh
# # print(s[::-1])  # hgfedcba
# # # Here last one is a step calculation by 2 from starting 



# def arr(s):
#     s = list(set(s))
#     s.sort()
#     return (s[-2])
# s = [1,2,3,4,5,3,9,8,90,70]
# print(arr(s))


arr = [1,2,3,4,90,4,0,4,300,450]
first = -999999
Second = -999999
for i in arr:
    if i > first:
        Second = first
        first = i
    elif i > Second and i != first:
        Second = i 
print(Second)
print(first)