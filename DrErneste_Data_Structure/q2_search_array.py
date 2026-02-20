def searching_in_array():
    print("=== Searching in an Array Tool ===")
    
    # Store 8 integers in an array
    # I'll initialize it with some values, but we can also Ask the user for them.
    # The prompt says "Create an array of 8 integers", so I'll ask for input.
    numbers = []
    print("Please enter 8 integers:")
    for i in range(8):
        while True:
            try:
                num = int(input(f"Enter integer {i+1}/8: "))
                numbers.append(num)
                break
            except ValueError:
                print("Error: Please enter a valid integer.")
    
    # Ask the user for a number to search
    try:
        search_target = int(input("\nEnter a number to search in the array: "))
        
        # Display whether the number exists and its index
        if search_target in numbers:
            index = numbers.index(search_target)
            print(f"Result: The number {search_target} exists in the array at index position {index}.")
        else:
            print(f"Result: The number {search_target} does NOT exist in the array.")
            
    except ValueError:
        print("Error: Search query must be an integer.")

if __name__ == "__main__":
    searching_in_array()
