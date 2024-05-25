n = int(input())
f1=1
f2=1
i=0
while i<n-1:
    f3=f1+f2
    f1=f2
    f2=f3
    i=i+1
print(f2)
