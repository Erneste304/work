# Ask user to enter a string
try:
    print("Program started. Waiting for your input...")
    text = input("Enter a string: ")  
except EOFError:
    
    print("Input not supported, using default text.")
    text = "hello world"


print("Your text has {} characters.".format(len(text)))