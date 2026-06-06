import numpy as np

print("MATRIX OPERATIONS TOOL")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of Matrix A:")
A = []
for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter elements of Matrix B:")
B = []
for i in range(rows):
    row = list(map(int, input().split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nAddition:")
print(A + B)

print("\nSubtraction:")
print(A - B)

print("\nMultiplication:")
print(np.dot(A, B))

print("\nTranspose of A:")
print(A.T)

print("\nDeterminant of A:")
print(np.linalg.det(A))