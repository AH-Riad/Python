# Transpose a Matrix (Simple Version)

# Input matrix dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input the matrix
matrix = []
print("\nEnter elements of the matrix:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Element [{i+1}][{j+1}]: ")))
    matrix.append(row)

# Print transpose
print("\nTranspose of the matrix:")
for j in range(cols):
    transposed_row = []
    for i in range(rows):
        transposed_row.append(matrix[i][j])
    print(transposed_row)
