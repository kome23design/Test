m=int(input("a number"))
n=int(input("a number"))
p=m*n
if(p<0):
    print("negative")
else:
    print("positive")
y=0
for i in range(10):
    x=int(input("enter a number"))
    y=y+x
print(f"the average is:{y/10}")