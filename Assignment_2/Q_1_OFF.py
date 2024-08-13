import pandas as pd
import numpy as np

#Q1.
df = pd.read_excel('purchase_data_1.xlsx')
matrixA = []
matrixB = []
matA = [1,2,3]
temp = []
dataframe1 = pd.read_excel('purchase_data_1.xlsx')
l = dataframe1.values
for i in range (0,len(l)):
    for j in range(1,5):
        if j in matA:
            temp.append(l[i][j])
        else:
            matrixB.append(l[i][j])
    matrixA.append(temp)
    temp = []
print(l)
print(dataframe1)
print("This is matrix A:")
print(matrixA)
print("THis is matrix B:")
print(matrixB)


#Q2.
row = len(matrixA)
column = len(matrixA[0])
print("The number of rows are: ",row)
print("THe number of columns are: ",column)

#Q3.
print("Number of vectors: ",row)

#Q4.
rank = np.linalg.matrix_rank(matrixA)
print("The rank of the matrix: ",rank)

#Q5.
A_pseudo = np.linalg.pinv(matrixA)
result = np.matmul(A_pseudo, matrixB)
print("The values are: ",result)



