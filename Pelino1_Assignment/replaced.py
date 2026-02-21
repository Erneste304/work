try:
    print("Welcome! Enter five texts to calculate their lengths (excluding spaces).\n")
    
    
    a = input("Enter first text A: ")
    b = input("Enter second text B: ")
    c = input("Enter third text C: ")
    d = input("Enter fourth text D: ")
    e = input("Enter fifth text E: ")
    
    
    texts = {"A": a, "B": b, "C": c, "D": d, "E": e}
    results = []
    
    for label, val in texts.items():
        clean_text = val.replace(" ", "")
        results.append(f"Length of {label} = {len(clean_text)}")
    
    
    print("\n" + ", ".join(results))

except KeyboardInterrupt:
    print("\n\nOperation cancelled. Goodbye!")
except EOFError:
    print("\nInput error. Please run in a standard terminal.")