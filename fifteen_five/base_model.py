"""Base Model for 15five."""

import os

import coreapi


class BaseModel:
    """Base Model."""

    def __init__(self):
        """Initialize 15five model."""
        auth = coreapi.auth.TokenAuthentication(token=os.environ['FIFTEEN_FIVE_TOKEN'])
        self.client = coreapi.Client(auth=auth)
