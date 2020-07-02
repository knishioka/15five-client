"""Base Model for 15five."""

import os

import coreapi


class BaseModel:
    """Base Model."""
    api_base_path = 'https://my.15five.com/api/public/'

    @classmethod
    def client(get, token=None):
        """Initialize 15five model."""
        if token is None:
            token = os.environ['FIFTEEN_FIVE_TOKEN']
        auth = coreapi.auth.TokenAuthentication(token=token)
        return coreapi.Client(auth=auth)
