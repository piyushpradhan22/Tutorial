# Armstrong Number
x =input('Input:')
l=len(x)
x=int(x)
x1=x
s = 0
while (x > 0):
    a = int(x % 10)
    s = s + (a **l)
    x = int(x/10)
if(s==x1):
    print('Output: Yes')
else:
    print('Output: No')