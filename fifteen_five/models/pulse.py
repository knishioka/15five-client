"""Pulse Model for 15five."""

from dateutil.parser import parse

from .base_model import BaseModel


class Pulse(BaseModel):
    """Pulse model."""

    api_path = BaseModel.api_base_path + "pulse/"
    valid_keys = ["id", "report", "user", "create_ts", "value"]

    def __init__(self, id, report, user, create_ts, value):
        """Initialize Pulse.

        Args:
            id (int): pulse id.
            report (str): Report url that created this pulse value.
            user (str): 15five user url.
            create_ts (str):  The actual date this answer was saved (submitted) by user.
            value (str): Pulse's value.

        """
        self.id = id
        self.report = report
        self.user = user
        self.create_ts = parse(create_ts)
        self.value = int(value)
