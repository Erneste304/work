class UserInfo:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality.strip().capitalize()
        
        # Dictionary of common country capitals
        self.capitals = {
            "Rwanda": "Kigali",
            "Uganda": "Kampala",
            "Kenya": "Nairobi",
            "Tanzania": "Dodoma",
            "Burundi": "Gitega",
            "France": "Paris",
            "USA": "Washington D.C.",
            "Canada": "Ottawa",
            "UK": "London",
            "China": "Beijing"
        }

    def display_info(self):
        print(f"\n--- User Profile ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Nationality: {self.nationality}")
        
        capital = self.capitals.get(self.nationality, "Unknown (not in our database)")
        print(f"The capital city of {self.nationality} is {capital}.")

def main():
    try:
        print("Welcome to the Country Info Tool!")
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        national = input("Enter your nationality (country): ")
        
        user = UserInfo(name, age, national)
        user.display_info()
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled. Goodbye!")

if __name__ == "__main__":
    main()


