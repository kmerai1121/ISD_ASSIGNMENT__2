"""Define the statuses available in the bank account."""

from emun import ENUM 

class AccountStatus(Enum):
    """Represents the possible status of an account """

    INACTIVE = 0
    ACTIVE = 1
    SUSPENDED = 2
    CLOSED = 3
    