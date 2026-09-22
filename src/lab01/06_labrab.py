n=int(input('in_1: '))
a=0
b=0
for i in range(n):
    i=input(f'in_{i+2}: ').split()
    if i[3]=='True':
        a+=1
    else:
        b+=1
print('out: ',a,b)