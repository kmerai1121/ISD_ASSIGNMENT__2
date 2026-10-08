"""Defines BankAccount class"""

from decimal import Decimal
from account.account_status import AccountStatus
from account.client import Client

class BankAccount:
    """Represent a bank account"""
    def __init__(self,
                 account_id: int,
                 balance: Decimal,
                 owner: Client,
                 status: AccountStatus
    ):
        """Initialize a bank account"""
        if account_id <= 0:
            raise ValueError("account_id must be a value greater than zero")
        self.__account_id = account_id
        self.__balance = balance
        self.__owner = owner
        self.__status = status

    @property
    def account_id(self) -> int:
        """Returns account_id"""
        return self.__account_id

    @property
    def balance(self) -> Decimal:
        """Returns current balance in the account"""
        return self.__balance

    @property
    def status(self) -> AccountStatus:
        """Returns account status"""
        return self.__status
    def update_balance(self,
                       amount: Decimal) -> None:
        """Update the account balance by specific amount"""
        self.__balance += amount

    def deposit(self,
                amount: Decimal) -> None:
        """Deposit a non negative amount into the account"""
        if amount < Decimal("0"):
            raise ValueError("amount must be a greater than or equal to zero")
        self.update_balance(amount)

    def withdraw(self,
                 amount: Decimal) -> None:
        """withdraw an amount from the account"""
        if amount < Decimal("0"):
            raise ValueError("amount must be greater than or equal to zero")

        if amount > self.__balance:
            raise ValueError("amount cannot exceed the account balance")

    def __str__(self) -> str:
        """Return the formatted account information"""
        return(
            f"Account Number: {self.__account_id}"
            f"Balance: ${self.__balance:,.2f}"
        )