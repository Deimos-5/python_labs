def min_max(nums):
    if not isinstance(nums,(list,tuple)):
        raise TypeError("TypeError")
    if len(nums)==0:
        raise ValueError("ValueError")
    mini=nums
    maxi=nums
    for num in nums:
        if not isinstance(num,(int,float)) or isinstance(num,bool):
            raise TypeError("TypeError")
        if num<mini:
            mini=num
        if num>maxi:
            maxi=num
    return mini,maxi

def unique_sorted(nums):
    if not isinstance(nums,(list,tuple)):
        raise TypeError("TypeError")
    for num in nums:
        if not isinstance(num,(int,float)) or isinstance(num,bool):
            raise TypeError("TypeError")
    if len(nums)==0:
        return []
    elems=[]
    for num in nums:
        if num not in elems:
            elems.append(num)
    for i in range(1,len(elems)):
        key=elems[i]
        j=i-1
        while j>=0 and elems[j]>key:
            elems[j+1]=elems[j]
            j-=1
        elems[j+1]=key
    return elems

def flatten(matrix):
    if not isinstance(matrix,(list,tuple)):
        raise TypeError("TypeError")
    nums=[]
    for row in matrix:
        if not isinstance(row,(list,tuple)):
            raise TypeError("строка не строка строк матрицы")
        for x in row:
            if not isinstance(x,(int,float)) or isinstance(x,bool):
                raise TypeError("TypeError")
            nums.append(x)
    return nums

print("min_max")
cases_min_max=[[3,-1,5,5,0],[42],[-5,-2,-9],[],[1.5,2,2.0,-3.1]]
for case in cases_min_max:
    try:
        res=min_max(case)
        print(f"{case} -> {res}")
    except Exception as e:
        print(f"{case} -> {type(e).__name__}")

print("\nunique_sorted")
cases_unique=[[3, 1, 2, 1, 3],[],[-1,-1,0,2,2],[1.0,1,2.5,2.5,0]]
for case in cases_unique:
    try:
        res=unique_sorted(case)
        print(f"{case} -> {res}")
    except Exception as e:
        print(f"{case} -> {type(e).__name__}")

print("\nflatten")
cases_flatten=[[[1, 2], [3, 4]],[[1, 2], (3, 4, 5)],[[1], [], [2, 3]],[[1, 2], "ab"]]
for case in cases_flatten:
    try:
        res=flatten(case)
        print(f"{case} -> {res}")
    except Exception as e:
        print(f"{case} -> {type(e).__name__}")
