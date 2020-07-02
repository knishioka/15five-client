"""User Model for 15five."""

from .base_model import BaseModel


class User(BaseModel):
    api_path = BaseModel.api_base_path + 'user/'

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

    @classmethod
    def all(cls):
        """Fetch user data.

        Returns:
            `list` of `User`

        """
        res = BaseModel.client().get(cls.api_path)
        # FIXME: Need to iterate when res['next'] is None.
        users = [User(id=u['id'], first_name=u['first_name'], last_name=u['last_name'], email=u['email'])
                 for u in res['results']]
        return users
