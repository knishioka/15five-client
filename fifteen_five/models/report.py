"""Report Model for 15five."""

from .base_model import BaseModel


class Report(BaseModel):
    """Report Model."""

    api_path = BaseModel.api_base_path + "report/"
    valid_keys = ["id", "user", "due_date"]

    def __init__(self, id, user, due_date):
        """Initialize user.

        Args:
            id (int): 15five report id.
            user (str): user that submitted this report.
            due_date (str): The actual date this report is/was due.

        """
        self.id = id
        self.user = user
        self.due_date = due_date
