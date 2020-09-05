"""Pulse Model for 15five."""

from dateutil.parser import parse

from .base_model import BaseModel
from .report import Report
from .user import User


class Pulse(BaseModel):
    """Pulse model.

    Examples:
        >>> pulses = Pulse.all(params={"created_on_start": "2020-09-01", "created_on_end": "2020-09-06"})
    """

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
        self._report = report
        self._user = user
        self.create_ts = parse(create_ts)
        self.value = int(value)

    @property
    def user(self):
        """Reported user."""
        return User.find_by_url(self._user)

    @property
    def report(self):
        """Pulse report."""
        return Report.find_by_url(self._report)
