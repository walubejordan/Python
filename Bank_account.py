class BankAccount:
    total_accounts = 0  # Class variable to track total accounts
    interest_rate = 0.05  # Class variable for interest rate

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1  # Increment total accounts when a new account is created
def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate

# Creating bank accounts
account1 = BankAccount("Joan", 10000)
account2 = BankAccount("Frank", 15000)

# Accessing class variables
print(BankAccount.total_accounts)  # Output: 2
print(BankAccount.interest_rate)  # Output: 0.05

# Applying interest to accounts
account1.apply_interest()
account2.apply_interest()

print(account1.balance)  # Output: 1050.0
print(account2.balance)  # Output: 1575.0
