class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.balance = initial_balance
        self.history = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.history.append(f"Deposit: +{amount}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.history.append(f"Withdraw: -{amount}")

    def transfer(self, amount: float, target_account: 'BankAccount'):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        target_account.balance += amount
        self.history.append(f"Transfer: {amount} to {target_account.owner}")
        target_account.history.append(f"Received: {amount} from {self.owner}")

    def get_balance(self) -> float:
        return self.balance
