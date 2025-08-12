# Program to add two matrices taking input from the user

# Input dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input first matrix
print("Enter elements of first matrix:")
matrix1 = []
for i in range(rows):
    row = list(map(int, input().split()))
    while len(row) != cols:
        print(f"Please enter exactly {cols} integers:")
        row = list(map(int, input().split()))
    matrix1.append(row)

# Input second matrix
print("Enter elements of second matrix:")
matrix2 = []
for i in range(rows):
    row = list(map(int, input().split()))
    while len(row) != cols:
        print(f"Please enter exactly {cols} integers:")
        row = list(map(int, input().split()))
    matrix2.append(row)

# Add the matrices
result = []
for i in range(rows):
    result_row = []
    for j in range(cols):
        result_row.append(matrix1[i][j] + matrix2[i][j])
    result.append(result_row)

# Display the result
print("Resultant matrix after addition:")
for row in result:
    print(" ".join(map(str, row)))
