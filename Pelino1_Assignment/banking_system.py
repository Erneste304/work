# bank_account.py

class Account:
    TRANSACTION_FEE = 1.00

    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount:.2f} to account {self.account_number}.")

    def withdraw(self, amount):
        total_deduction = amount + self.TRANSACTION_FEE
        if total_deduction <= self.balance:
            self.balance -= total_deduction
            print(f"Withdrew {amount:.2f} (plus {self.TRANSACTION_FEE:.2f} fee) from account {self.account_number}.")
        else:
            print(f"Insufficient funds (required {total_deduction:.2f} including fee).")



    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account {self.account_number} Holder: {self.holder_name} Balance: {self.balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, interest_rate, initial_balance=0):
        super().__init__(account_number, holder_name, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest of {interest:.2f} added to account {self.account_number}.")

    def get_interest_projections(self, amount):
        print(f"\nInterest projections for {amount:.2f} at {self.interest_rate}% annual rate:")
        months = [1, 3, 6, 12]
        monthly_rate = (self.interest_rate / 100) / 12
        for m in months:
            projected_interest = amount * monthly_rate * m
            print(f"  {m} Month(s): {projected_interest:.2f}")


    def __str__(self):
        return (f"Savings Account {self.account_number} Holder: {self.holder_name} "
                f"Balance: {self.balance:.2f} Interest Rate: {self.interest_rate:.1f}")


class CheckingAccount(Account):
    def __init__(self, account_number, holder_name, overdraft_limit, initial_balance=0):
        super().__init__(account_number, holder_name, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        
        total_deduction = amount + self.TRANSACTION_FEE
        if total_deduction > self.balance + self.overdraft_limit:
            print(f"Withdrawal of {amount:.2f} exceeds overdraft limit (total deduction including fee: {total_deduction:.2f}).")
        else:
            self.balance -= total_deduction
            print(f"Withdrew {amount:.2f} (plus {self.TRANSACTION_FEE:.2f} fee) from account {self.account_number}.")


    def __str__(self):
        return (f"Checking Account {self.account_number} Holder: {self.holder_name} "
                f"Balance: {self.balance:.2f} Overdraft Limit: {self.overdraft_limit:.2f}")


def main_menu():
    accounts = {}
    
    try:
        while True:
            print("\n=== Banking System Menu ===")
            print("1. Create Savings Account")
            print("2. Create Checking Account")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. View Account Details")
            print("6. Project Interest (Savings)")
            print("7. Exit")
            
            choice = input("Enter choices (1-7): ")
            
            if choice == "7":
                print("Thank you for using the Banking System. Goodbye!")
                break
                
            if choice in ["1", "2"]:
                acc_num = input("Enter account number: ")
                if acc_num in accounts:
                    print(f"Error: Account number {acc_num} already exists.")
                    continue
                    
                name = input("Enter holder name: ")
                try:
                    balance = float(input("Enter initial balance: "))
                    if choice == "1":
                        rate = float(input("Enter interest rate (%): "))
                        accounts[acc_num] = SavingsAccount(acc_num, name, rate, balance)
                    else:
                        limit = float(input("Enter overdraft limit: "))
                        accounts[acc_num] = CheckingAccount(acc_num, name, limit, balance)
                    print(f"Account {acc_num} created successfully.")
                except ValueError:
                    print("Error: Invalid amount entered. Please use numbers.")
                
            elif choice in ["3", "4", "5", "6"]:
                acc_num = input("Enter account number: ")
                if acc_num not in accounts:
                    print("Account not found.")
                    continue
                
                account = accounts[acc_num]
                
                try:
                    if choice == "3":
                        amount = float(input("Enter deposit amount: "))
                        account.deposit(amount)
                    elif choice == "4":
                        amount = float(input("Enter withdrawal amount: "))
                        account.withdraw(amount)
                    elif choice == "5":
                        print(account)
                    elif choice == "6":
                        if isinstance(account, SavingsAccount):
                            amount = float(input("Enter amount to project: "))
                            account.get_interest_projections(amount)
                        else:
                            print("This feature is only available for Savings Accounts.")
                except ValueError:
                    print("Error: Invalid amount entered. Please use numbers.")
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted (Ctrl+C). Saving session and exiting...")
        print("Thank you for using the Banking System. Goodbye!")

if __name__ == "__main__":
    main_menu()




