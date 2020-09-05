"""Report Model for 15five."""

from .base_model import BaseModel


class Report(BaseModel):
    """Report Model.

    Examples:
        >>> Report.all(params={"due_date_start": "2020-09-01", "due_date_end": "2020-09-06"})
    """

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
        self._user = user
        self.due_date = due_date
