def matrix_addition():
    print("=== Matrix Addition (2x2) Tool ===")
    
    def input_matrix(name):
        print(f"\nEnter elements for Matrix {name} (2x2):")
        matrix = []
        for i in range(2):
            row = []
            for j in range(2):
                while True:
                    try:
                        val = float(input(f"Enter element [{i}][{j}]: "))
                        row.append(val)
                        break
                    except ValueError:
                        print("Error: Invalid input. Enter a number.")
            matrix.append(row)
        return matrix

    # Input Matrix 1 and 2
    matrix1 = input_matrix("1")
    matrix2 = input_matrix("2")

    # Perform Matrix Addition
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    # Display Result
    print("\nResulting Matrix (1 + 2):")
    for row in result:
        print(row)

if __name__ == "__main__":
    matrix_addition()
