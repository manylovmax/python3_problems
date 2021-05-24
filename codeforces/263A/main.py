from math import fabs

TARGET_VALUE = 3
MATRIX_SIZE = 5

matrix = {}
x = y = 0

for i in range(MATRIX_SIZE):
    matrix[i] = [int(x) for x in input().split()]
    for j in range(MATRIX_SIZE):
        if matrix[i][j] == 1:
            x = j + 1
            y = i + 1

res = fabs(TARGET_VALUE - x) + fabs(TARGET_VALUE - y)

print(int(res))
