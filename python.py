a=int(input("enter first number"))
b=int(input("enter second number"))
print("1:addition, 2:substraction, 3:multiplication, 4:division")
choice = int(input("enter your choice"))
if(choice == 1):
    print(a+b)
elif(choice == 2):
    print(a-b)
elif(choice == 3):
    print(a*b)
elif(choice == 4):
    print(a/b)
else:
    print("invalid choice")