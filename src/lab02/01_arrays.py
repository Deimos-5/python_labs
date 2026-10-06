def min_max(nums1: list[float | int]) -> tuple[float | int, float | int]:
    nums1=nums1[1:-1].split(', ')
    nums=[]
    for x in nums1:
        if x=='':
            break
        if '.' in x:
            nums.append(float(x))
        else:
            nums.append(int(x))
    if len(nums)==0:
        raise ValueError("ValueError")
    mini=nums[0]
    maxi=nums[0]
    for num in nums:
        if num<mini:
            mini=num
        if num>maxi:
            maxi=num
    return mini, maxi

def unique_sorted(nums1: list[float | int]) -> list[float | int]:
    nums1=nums1[1:-1].split(', ')
    nums=[]
    for x in nums1:
        if x=='':
            break
        if '.' in x:
            nums.append(float(x))
        else:
            nums.append(int(x))
    if len(nums)==0:
        return []
    elems=[]
    for num in nums:
        if num not in elems:
            elems.append(num)
    for i in range(1, len(elems)):
        key=elems[i]
        j=i-1
        while j>=0 and elems[j]>key:
            elems[j+1]=elems[j]
            j-=1
        elems[j+1]=key
    return elems

def flatten(nums1: list[list | tuple]) -> list:
    s=nums1.replace('[','').replace(']','').replace('(','').replace(')','')
    nums1=s.split(', ')
    nums=[]
    for x in nums1:
        if x!='':
            try:
                if '.' in x:
                    nums.append(float(x))
                else:
                    nums.append(int(x))
            except ValueError:
                raise TypeError('TypeError')
    return nums

a=input("Впишите одномерный массив с числами (для min_max или unique_sorted) или двумерный массив (для flatten): ")
if '[[' not in a:
    print(f'min_max: {min_max(a)}')
    print(f'unique_sorted: {unique_sorted(a)}')
print(f'flatten: {flatten(a)}')