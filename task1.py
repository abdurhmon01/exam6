a = [10, 15, 20, 22, 10, 6]
m=-99999999999999
n=99999999999999
for i in range(len(a)):
    if a[i]>m:m=a[i]
    if a[i]<m:n=a[i]
print("max:",m, "min:",n)
print("diferense:",m-n)