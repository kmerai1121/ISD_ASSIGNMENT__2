"""Defines client class"""

from email_validator import validate_email

class Client:
    """Represent a banking client"""
    def __init__(self, 
                 client_id:int,
                 name: str,
                 email_address: str):
        """Initialize a client with an ID, name and email address"""
        if client_id < = 0:
            raise ValueError("client_id must be a value greater than zero")
        if not name.strip():
            raise ValueError("name cannot be empty")

        validated_emial = validate_email( email_address, check_deliverability = False)

        self.__client_id = client_id
        self.__name = name
        self.__email_address = validated_email.normalized

    @property
    def client_id(self) -> int:
        """Returns client's ID"""
        return self.__client_id 

    @property
    def name(self) -> str:
        """Returns client's name"""
        return self.__name

    @property
    def email_addreess(self) -> str:
        """Returns client's email address"""
        return self.__email_address

    def __str__(self) -> str:
        """Returns formatted information"""
        return(f"{self.__name}"
               f"[{self.__client_id}] -"
               f"{self.__email_address}")
    