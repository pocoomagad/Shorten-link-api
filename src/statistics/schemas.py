from src.schemas import BaseSchema

from datetime import datetime

class LogLinkSchema(BaseSchema):
    id: int
    time_click: datetime

class StatisticsLinkSchema(BaseSchema):
    id: int
    list_of_actions: list[LogLinkSchema]
    count_clicks: int
    time_of_last_click: datetime
    creation_date: datetime