def reverse_array():
    print("=== Reverse an Array Tool ===")
    
    # Store 6 numbers in an array
    numbers = []
    print("Please enter 6 numbers:")
    for i in range(6):
        while True:
            try:
                val = float(input(f"Enter number {i+1}/6: "))
                numbers.append(val)
                break
            except ValueError:
                print("Error: Please enter a valid number.")
    
    # Display the array in original order
    print("\nOriginal order:", numbers)
    
    # Display the array in reverse order
    # Using list slicing to reverse
    reversed_numbers = numbers[::-1]
    print("Reverse order: ", reversed_numbers)

if __name__ == "__main__":
    reverse_array()
