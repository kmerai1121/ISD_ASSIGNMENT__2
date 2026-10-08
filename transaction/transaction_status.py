"""Defines the possible transaction statuses"""

from enum import Enum 

class TransactionStatus(Enum):
    """Represent the possible statuses of transaction"""

    PENDING = 1
    PROCESSED = 2
    FAILED =3
    