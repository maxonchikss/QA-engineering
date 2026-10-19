import pytest
from src.bank_account import BankAccount


def test_create_account():
    account = BankAccount("Alice", 1000.0)
    assert account.owner == "Alice"
    assert account.get_balance() == 1000.0


def test_deposit():
    account = BankAccount("Alice", 1000.0)
    account.deposit(500.0)
    assert account.get_balance() == 1500.0


def test_deposit_negative():
    account = BankAccount("Alice", 1000.0)
    with pytest.raises(ValueError):
        account.deposit(-100.0)


def test_withdraw():
    account = BankAccount("Alice", 1000.0)
    account.withdraw(300.0)
    assert account.get_balance() == 700.0


def test_withdraw_insufficient_funds():
    account = BankAccount("Alice", 1000.0)
    with pytest.raises(ValueError):
        account.withdraw(1500.0)


def test_transfer():
    alice = BankAccount("Alice", 1000.0)
    bob = BankAccount("Bob", 500.0)
    alice.transfer(300.0, bob)
    assert alice.get_balance() == 700.0
    assert bob.get_balance() == 800.0


def test_transfer_insufficient_funds():
    alice = BankAccount("Alice", 1000.0)
    bob = BankAccount("Bob", 500.0)
    with pytest.raises(ValueError):
        alice.transfer(1500.0, bob)


def test_transfer_negative():
    alice = BankAccount("Alice", 1000.0)
    bob = BankAccount("Bob", 500.0)
    with pytest.raises(ValueError):
        alice.transfer(-100.0, bob)
