def checkprime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
            break
        
    return True
num = 17
result = checkprime(num)
print(result)