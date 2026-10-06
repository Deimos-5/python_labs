def matrix(mat_str):
    if mat_str=='[]' or mat_str=='':
        return []
    s=mat_str[1:-1]
    rows1=s.split('], [')
    if len(rows1)==1 and rows1==s:
        rows1=s.split('), (')
    mat=[]
    for row in rows1:
        row1=row.replace('[','').replace(']','').replace('(','').replace(')','')
        if row1!='':
            row_nums=[]
            for x in row1.split(', '):
                if '.' in x:
                    row_nums.append(float(x))
                else:
                    row_nums.append(int(x))
            mat.append(row_nums)
    if len(mat)>0:
        row_len=len(mat[0])
        for r in mat:
            if len(r)!=row_len:
                raise ValueError('ValueError')
    return mat

def transpose(mat_str: list[list[float | int]]) -> list[list]:
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

def row_sums(mat_str: list[list[float | int]]) -> list[float]:
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

def col_sums(mat_str: list[list[float | int]]) -> list[float]:
    mat=matrix(mat_str)
    if not mat:
        return []
    res=[0]*len(mat[0])
    for row in mat:
        for j in range(len(row)):
            res[j]+=row[j]
    return res

a=input("Впишите прямоугольную матрицу: ")
print(f'transpose: {transpose(a)}')
print(f'row_sums: {row_sums(a)}')
print(f'col_sums: {col_sums(a)}')