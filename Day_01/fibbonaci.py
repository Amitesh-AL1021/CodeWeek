def fibbo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbo(n-1) + fibbo(n-2)
n = 3 
result = fibbo(n)
print(result)


num = 23 
a , b = 0 , 1 
for i in range(num):
    a,b = b , a+b
    print(a,end=" ")
