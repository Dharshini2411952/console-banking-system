from dataclasses import dataclass

@dataclass
class Account:
    acc_id: int
    name: str
    balance: float