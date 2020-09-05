"""Base Model for 15five."""

import os

import coreapi


class BaseModel:
    """Base Model."""

    api_base_path = "https://my.15five.com/api/public/"
    valid_keys = []

    @classmethod
    def client(cls, token=None):
        """Initialize 15five model."""
        if token is None:
            token = os.environ["FIFTEEN_FIVE_TOKEN"]
        auth = coreapi.auth.TokenAuthentication(token=token)
        return coreapi.Client(auth=auth)

    @classmethod
    def row_all(cls):
        """Fetch all results."""
        res = cls.client().get(cls.api_path)
        results = res["results"]
        while next_path := res["next"]:
            res = cls.client().get(next_path)
            results += res["results"]
        return results

    @classmethod
    def find(cls, id):
        """Find data by id."""
        res = cls.client().get(f"{cls.api_path}{id}")
        return cls.from_dict(res)

    @classmethod
    def find_by_url(cls, url):
        """Find data by url."""
        res = cls.client().get(url)
        return cls.from_dict(res)

    @classmethod
    def all(cls):
        """Fetch all data as model class."""
        return [cls.from_dict(row) for row in cls.row_all()]

    @classmethod
    def from_dict(cls, result_dict):
        """Create instance from dict.

        Args:
            result_dict (dict): API results.

        Returns:
            BaseModel

        """
        return cls(**cls.valid_args(result_dict))

    @classmethod
    def valid_args(cls, result_dict):
        """Extract valid key value pairs.

        Args:
            result_dict (dict): API results.

        Returns:
            dict: dict including only valid keys.

        """
        return {key: result_dict[key] for key in cls.valid_keys}
