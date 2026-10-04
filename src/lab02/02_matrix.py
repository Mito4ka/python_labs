#02_matrix
"""
def transpose(mat: list[list[float | int]]) -> list[list]:
   
    for row in mat:
        if len(row) != len(mat[0]):
            raise ValueError('«матрица рваная» (строки разной длины)')
    if mat == []:
        return []
    cnt_stolb = len(mat[0])

    ans = []
    for j in range(cnt_stolb):
        a = []
        for row in mat:
            a.append(row[j])
        ans.append(a)
    return ans
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))

def row_sums(mat: list[list[float | int]]) -> list[float]:

    for row in mat:
        if len(row)!=len(mat[0]):
            raise ValueError('pваная матрица')
    ans=[]
    for row in mat:
        ans.append(sum(row))
    return ans
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3],]))
"""
def col_sums(mat: list[list[float | int]]) -> list[float]:


    for row in mat:
        if len(row) != len(mat[0]):
            raise ValueError('рваная матрица')
    ans = []
    stolbec = len(mat[0])
    for j in range(stolbec):
        cnt = 0
        for row in mat:
            cnt += row[j]
        ans.append(cnt)
    return ans
print(col_sums([[1,2,3],[4,5,6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))