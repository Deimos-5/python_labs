def matrix(mat):
    if not isinstance(mat,(tuple,list)):
        raise TypeError('TypeError')
    if not mat:
        return []
    res=[]
    for row in mat:
        if not isinstance(row,(tuple,list)):
            raise TypeError('TypeError')
        new_row=[]
        for x in row:
            if not isinstance(x,(int,float)) or isinstance(x,bool):
                raise TypeError('TypeError')
            new_row.append(x)
        res.append(new_row)
    row_len=len(res[0])
    for r in res:
        if len(r)!=row_len:
            raise ValueError('ValueError')
    return res

def transpose(mat_str):
    mat=matrix(mat_str)
    if not mat:
        return []
    res=[]
    for j in range(len(mat[0])):
        new_row=[]
        for i in range(len(mat)):
            new_row.append(mat[i][j])
        res.append(new_row)
    return res

def row_sums(mat_str):
    mat=matrix(mat_str)
    if not mat:
        return []
    res=[]
    for row in mat:
        s=0
        for x in row:
            s+=x
        res.append(s)
    return res

def col_sums(mat_str):
    mat=matrix(mat_str)
    if not mat:
        return []
    res=[0]*len(mat[0])
    for row in mat:
        for j in range(len(row)):
            res[j]+=row[j]
    return res

print("transpose")
cases_transpose=[[[1, 2, 3]], [[1], [2], [3]], [[1, 2], [3, 4]], [], [[1, 2], [3]]]
for case in cases_transpose:
    try:
        res=transpose(case)
        print(f"{case} -> {res}")
    except Exception as e:
        print(f"{case} -> {type(e).__name__}")

print("\nrow_sums")
cases_row_sums=[[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]]
for case in cases_row_sums:
    try:
        res=row_sums(case)
        print(f"{case} -> {res}")
    except Exception as e:
        print(f"{case} -> {type(e).__name__}")

print("\ncol_sums")
cases_col_sums=[[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]]
for case in cases_col_sums:
    try:
        res=col_sums(case)
        print(f"{case} -> {res}")
    except Exception as e:
        print(f"{case} -> {type(e).__name__}")