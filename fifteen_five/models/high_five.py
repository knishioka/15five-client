"""HighFive Model for 15five."""

from dateutil.parser import parse

from .base_model import BaseModel


class HighFive(BaseModel):
    """HighFive model."""

    api_path = BaseModel.api_base_path + "high-five/"
    valid_keys = ["id", "report", "create_ts", "text"]

    def __init__(self, id, report, create_ts, text):
        """Initialize high five.

        Args:
            id (int): High Five id.
            report (str): Report that contains the high five.
            create_ts (str): The actual date this high five was saved (submitted) by user.
            text (str): High Five content.

        """
        self.id = id
        self.report = report
        self.create_ts = parse(create_ts)
        self.text = text
