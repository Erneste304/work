def kajipotefu_cipher(text, mode='encode'):
    # Mapping: a->k, i->j, o->p, e->t, u->f
    mapping = {
        'a': 'k', 'i': 'j', 'o': 'p', 'e': 't', 'u': 'f',
        'A': 'K', 'I': 'J', 'O': 'P', 'E': 'T', 'U': 'F'
    }
    
    if mode == 'decode':
        # Reverse the mapping
        mapping = {v: k for k, v in mapping.items()}
    
    result = ""
    for char in text:
        result += mapping.get(char, char)
    return result

def main():
    try:
        print("=== Kajipotefu Cipher Tool ===")
        while True:
            print("\n1. Encode (Normal -> Kajipotefu)")
            print("2. Decode (Kajipotefu -> Normal)")
            print("3. Exit")
            
            choice = input("Select an option (1-3): ")
            
            if choice == "3":
                print("Goodbye!")
                break
            
            if choice in ["1", "2"]:
                mode = 'encode' if choice == "1" else 'decode'
                prompt = "Enter text to encode: " if mode == 'encode' else "Enter text to decode: "
                text = input(prompt)
                
                result = kajipotefu_cipher(text, mode)
                print(f"\nResult: {result}")
            else:
                print("Invalid choice. Please try again.")
                
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")

if __name__ == "__main__":
    main()
