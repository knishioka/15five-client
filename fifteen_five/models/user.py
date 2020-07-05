"""User Model for 15five."""

from .base_model import BaseModel


class User(BaseModel):
    """Use model."""

    api_path = BaseModel.api_base_path + "user/"
    valid_keys = ["id", "first_name", "last_name", "email"]

    def __init__(self, id, first_name, last_name, email):
        """Initialize user.

        Args:
            id (int): 15five user id.
            first_name (str): user first name.
            last_name (str): user last name.
            email (str): user email address.

        """
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
