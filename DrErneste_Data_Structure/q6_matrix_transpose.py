def matrix_transpose():
    print("=== Transpose of a Matrix Tool ===")
    
    # Create a 3x3 matrix
    matrix = []
    print("Please enter elements for a 3x3 Matrix:")
    for i in range(3):
        row = []
        for j in range(3):
            while True:
                try:
                    val = float(input(f"Enter element [{i}][{j}]: "))
                    row.append(val)
                    break
                except ValueError:
                    print("Error: Invalid number.")
        matrix.append(row)
    
    # Display the original matrix
    print("\nOriginal Matrix:")
    for row in matrix:
        print(row)
    
    # Calculate and Display its transpose
    # Transposing means swapping matrix[i][j] with matrix[j][i]
    transpose = [[0, 0, 0] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            transpose[j][i] = matrix[i][j]
            
    print("\nTranspose Matrix:")
    for row in transpose:
        print(row)

if __name__ == "__main__":
    matrix_transpose()
