"""x= int(input("interger number"))
if(x<0):
    print("the number in negative")
elif(x>=0):
    print("the number in positive")
y= int(input("interger number"))
c=x+y
print(c)

x=input("enter a day")
if(x=="monday"):
    print("fried rice = 2000f")
elif(x=="tuesday"):
    print("poulet dg")
elif(x=="wednesday"):
    print("okro")
    print("ekwang")

x = input("enter a word")
for m in range(len(x)):
    if (m%2==0):
        print(x[m])"""

c=0
for k in range(10):
    if ((k+c)%3 !=0):
        print(k+c)
        c=k