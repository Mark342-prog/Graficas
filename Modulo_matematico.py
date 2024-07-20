#Este py es la base para trabajo de matrices 
def mult_matrx(a, b):
    matrix1 = a
    matrix2 = b
    rango1 = len(matrix1[0])
    rango2 = len(matrix2)
    rango3 = len(matrix1)
    rango4 = len(matrix2[0])
    if rango1 == rango2:
        res = [[0 for x in range(rango4)] for y in range(rango3)] 
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    res[i][j] += matrix1[i][k] * matrix2[k][j]
        return res
    if rango3 == rango4:
        res = [[0 for x in range(rango2)] for y in range(rango1)] 
        for i in range(len(matrix2)):
            for j in range(len(matrix1[0])):
                for k in range(len(matrix1)):
                    res[i][j] += matrix2[i][k] * matrix1[k][j]
    else: 
        return print("no valido")


matrix1 = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]
matrix2 = [[5,8,1,0],
        [6,7,3,0],
        [4,5,9,0]]

print (mult_matrx(matrix1, matrix2))