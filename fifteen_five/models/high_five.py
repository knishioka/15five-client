"""HighFive Model for 15five."""

from dateutil.parser import parse

from .base_model import BaseModel


class HighFive(BaseModel):
    """HighFive model."""
    api_path = BaseModel.api_base_path + 'high-five/'

    def __init__(self, id, report, create_ts, text):
        """Initialize high five.

        Args:
            id (int): High Five id.
            report (str): Report that contains the high five.
            create_ts (datetime): The actual date this high five was saved (submitted) by user.
            text (str): High Five content.

        """
        self.id = id
        self.report = report
        self.create_ts = create_ts
        self.text = text

    @classmethod
    def all(cls):
        """Fetch high five.

        Returns:
            `list` of `HighFive`

        """
        results = cls.row_all()
        high_fives = [HighFive(id=hf['id'], report=hf['report'], create_ts=parse(hf['create_ts']), text=hf['text'])
                      for hf in results]
        return high_fives
