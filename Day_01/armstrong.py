num = 153
original = num

power = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total += digit ** power
    num = num // 10

if total == original:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")