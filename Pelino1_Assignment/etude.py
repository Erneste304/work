# Ask user to enter a string
try:
    print("Program started. Waiting for your input...")
    text = input("Enter a string: ")  # Works in terminal
except EOFError:
    # For environments that don't support input()
    print("Input not supported, using default text.")
    text = "hello world"

# Print the length of the string
print("Your text has {} characters.".format(len(text)))