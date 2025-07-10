d={}
for i in range (3):
   name=(input("enter the name:"))
   mark=int(input("enter the mark:"))
   d[name]=mark
print(d)
for i in d:
   if d[i]>90:
      print("A")
   elif d[i]>80:
      print("B")
   elif d[i]>70:
      print("C")
   else:
      print("D")