a=int(input("enter the number:"))
flag=0
for i in range (2,a):
    if a % i == 0:
        flag = 1
        break
if flag == 0:
    print(a, "is a prime number")
else:
    print(a, "is not a prime number")
    