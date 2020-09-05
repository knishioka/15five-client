"""Report Model for 15five."""

from .base_model import BaseModel


class Report(BaseModel):
    """Report Model.

    Examples:
        >>> Report.all(params={"due_date_start": "2020-09-01", "due_date_end": "2020-09-06"})
    """

    api_path = BaseModel.api_base_path + "report/"
    valid_keys = [
        "id",
        "user",
        "due_date",
        "reporting_period",
        "reporting_period_start",
        "reporting_period_end",
        "submit_ts",
        "was_submitted_late",
    ]

    def __init__(
        self,
        id,
        user,
        due_date,
        reporting_period,
        reporting_period_start,
        reporting_period_end,
        submit_ts,
        was_submitted_late,
    ):
        """Initialize user.

        Args:
            id (int): 15five report id.
            user (str): user that submitted this report.
            due_date (str): The actual date this report is/was due.
            reporting_period (str): Reporting period.
            reporting_period_start (str): Reporting period start timestamp.
            reporting_period_end (str): Reporting period end timestamp.
            submit_ts (str): Reported timestamp.
            was_submitted_late (bool): whether the report was submitted late.

        """
        self.id = id
        self._user = user
        self.due_date = due_date
        self.reporting_period = reporting_period
        self.reporting_period_start = reporting_period_start
        self.reporting_period_end = reporting_period_end
        self.submit_ts = submit_ts
        self.was_submitted_late = was_submitted_late
