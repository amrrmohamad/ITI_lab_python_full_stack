class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"The amount is {amount}. New balance is {self.balance}.")
        else:
            print(" Amount must be positive and less than or equal to the balance.")

    def __str__(self):
        return f"Account owner: {self.owner} \n = Account balance: {self.balance}"


class SavingsAccount(Account):
    def apply_present(self, rate):
        if rate > 0:
            present = self.balance * rate
            self.balance += present
            print(f"Applied present at rate {rate}. New balance is : {self.balance}.")
        else:
            print("present rate must be positive.")


class CheckingAccount(Account):
    pass


# Example Usage
myacc_savings = SavingsAccount("Someone", 1000)
myacc_savings.deposit(500)
myacc_savings.apply_present(0.05)
myacc_savings.withdraw(300)
print(myacc_savings) #  Account owner: SomeoneAccount balance: 1500.0

myacc_checking = CheckingAccount("SomeoneElse", 200)
myacc_checking.deposit(100)
myacc_checking.withdraw(50)
print(myacc_checking) # Account owner: SomeoneElse\nAccount balance: 150.0"}
