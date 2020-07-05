"""Base Model for 15five."""

import os

import coreapi


class BaseModel:
    """Base Model."""
    api_base_path = 'https://my.15five.com/api/public/'

    @classmethod
    def client(cls, token=None):
        """Initialize 15five model."""
        if token is None:
            token = os.environ['FIFTEEN_FIVE_TOKEN']
        auth = coreapi.auth.TokenAuthentication(token=token)
        return coreapi.Client(auth=auth)

    @classmethod
    def row_all(cls):
        """Get all results."""
        res = cls.client().get(cls.api_path)
        results = res['results']
        while next_path := res['next']:
            res = cls.client().get(next_path)
            results += res['results']
        return results
