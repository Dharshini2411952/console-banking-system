from dataclasses import dataclass


@dataclass
class Account:
    acc_id: int
    name: str
    balance: float


@dataclass
class Transaction:
    from_id: int
    to_id: int
    amount: float