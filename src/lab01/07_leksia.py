a=input()
b=''
z=0
for i in range(len(a)):
    if b=='':
        if a[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            b+=a[i]
            k=i
    elif len(b)==1:
        if a[i] in '0123456789':
            b+=a[i+1]
            z=i+1-k
    else:
        m=i+z
        while a[m]!='.':
            b+=a[m]
            m=m+z
        break
print(b+'.')