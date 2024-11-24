x = int(input("Enter an interger"))
if x<0:
    x=0
    print("Negative changed to zero")
elif x==0:
    print("Zero")
elif x==1:
    print("Single")
else:
    print("More")
words = ["cats", "window", "defenestrate"]
for w in words:
    print(w, len(w))
for w in words[:]:
    if len(w) > 6:
        words.insert(0, W)
a = ['mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

def add(a, b):
    c = 0
    c = a+b
    return c

x=add(2, 7)  
print(x)
def evenodd(n):
    if(n%2 == 0):
        print(n, "is even number")
    else:
        print(n, "is odd number")
evenodd(12)
def prime(n):
    if ((n%2==0) or (n%3==0)):
        print(n, "is not a prime number")
    else:
        print(n, "is a prime number")
prime(9)