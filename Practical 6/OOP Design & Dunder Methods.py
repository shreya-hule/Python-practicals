# Practical 6: OOP Design & Dunder Methods

# Class Design Notes:
# Fields: holder, account_number, _balance
# Methods: deposit, withdraw, get_balance, transfer_to
# Dunder Methods: __init__, __str__, __repr__, __add__
# Validation: No negative balances, invalid deposits,
# or withdrawals exceeding the balance.
# The + operator adds balances without changing accounts.


class BankAccount:

    # Constructor
    def __init__(self, holder, account_number, opening_balance=0.0):
        if not isinstance(holder, str) or not holder.strip():
            raise ValueError("Account holder cannot be blank")

        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative")

        self.holder = holder
        self.account_number = account_number
        self._balance = float(opening_balance)

    # Get balance
    def get_balance(self):
        return self._balance

    # Extension 2: Read-only balance property
    @property
    def balance(self):
        return self._balance

    # Deposit money
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self._balance += amount
        print(f"Deposited: Rs. {amount:.2f}")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount
        print(f"Withdrawn: Rs. {amount:.2f}")

    # Extension 1: Transfer money
    def transfer_to(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("Invalid destination account")

        if amount <= 0:
            raise ValueError("Transfer amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        if self is other_account:
            raise ValueError("Cannot transfer to the same account")

        self._balance -= amount
        other_account._balance += amount

        print(f"Transferred Rs. {amount:.2f} to {other_account.holder}")

    # Human-readable representation
    def __str__(self):
        return f"BankAccount({self.holder}, balance=Rs. {self._balance:.2f})"

    # Developer representation
    def __repr__(self):
        return (
            f"BankAccount(holder={self.holder!r}, "
            f"account_number={self.account_number!r}, "
            f"opening_balance={self._balance!r})"
        )

    # Operator overloading
    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented

        return self._balance + other._balance


# Extension 3: Student class
class Student:

    def __init__(self, name, roll_number, marks):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name cannot be blank")

        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100")

        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"

    def __repr__(self):
        return (
            f"Student(name={self.name!r}, "
            f"roll_number={self.roll_number!r}, "
            f"marks={self.marks!r})"
        )


# Main program
def main():

    print("===== PRACTICAL 6: OOP & DUNDER METHODS =====")

    # Creating objects
    account1 = BankAccount("Asha", "BA101", 1500)
    account2 = BankAccount("Kabir", "BA102", 500)

    print("\n1. Initial Accounts")
    print(account1)
    print(account2)

    # Deposit
    print("\n2. Deposit")
    account1.deposit(250)
    print("Balance:", account1.get_balance())

    # Withdrawal
    print("\n3. Withdrawal")
    account2.withdraw(100)
    print("Balance:", account2.get_balance())

    # Dunder methods
    print("\n4. Dunder Methods")
    print("str:", str(account1))
    print("repr:", repr(account1))

    # Operator overloading
    print("\n5. Operator Overloading")
    print("Combined Balance:", account1 + account2)

    # Extension 1: Transfer
    print("\n6. Transfer Money")
    account1.transfer_to(account2, 300)

    print("Asha Balance:", account1.balance)
    print("Kabir Balance:", account2.balance)

    # Extension 2: Read-only property
    print("\n7. Read-Only Balance")
    print("Current Balance:", account1.balance)

    try:
        account1.balance = 5000
    except AttributeError:
        print("Error: Cannot directly modify balance")

    # Invalid operation 1
    print("\n8. Invalid Deposit")
    try:
        account1.deposit(-100)
    except ValueError as e:
        print("Error:", e)

    # Invalid operation 2
    print("\n9. Invalid Withdrawal")
    try:
        account1.withdraw(10000)
    except ValueError as e:
        print("Error:", e)

    # Invalid operation 3
    print("\n10. Invalid Transfer")
    try:
        account1.transfer_to(account2, -200)
    except ValueError as e:
        print("Error:", e)

    # Extension 3: Student class
    print("\n11. Student Class")
    student1 = Student("Keshav", 101, 95)

    print(student1)
    print(repr(student1))

    # Extension 4: Verify no mutation
    print("\n12. Addition Does Not Modify Accounts")
    before1 = account1.balance
    before2 = account2.balance

    total = account1 + account2

    print("Combined Balance:", total)
    print("Asha Balance Unchanged:", before1 == account1.balance)
    print("Kabir Balance Unchanged:", before2 == account2.balance)

    print("\n===== PRACTICAL COMPLETED =====")


if __name__ == "__main__":
    main()