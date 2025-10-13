# Add Two Matrices (Simple Version)

# Input matrix dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input first matrix
print("\nEnter elements of first matrix:")
matrix1 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Element [{i+1}][{j+1}]: ")))
    matrix1.append(row)

# Input second matrix
print("\nEnter elements of second matrix:")
matrix2 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Element [{i+1}][{j+1}]: ")))
    matrix2.append(row)

# Add the two matrices
print("\nSum of the two matrices:")
for i in range(rows):
    sum_row = []
    for j in range(cols):
        sum_row.append(matrix1[i][j] + matrix2[i][j])
    print(sum_row)
