n=int(input())
a=0
b=0
for i in range(n):
    i=input().split()
    if i[3]=='True':
        a+=1
    else:
        b+=1
print(a,b)