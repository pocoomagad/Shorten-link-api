from pydantic import HttpUrl, ConfigDict

from src.schemas import BaseSchema

class LinkDTO(BaseSchema):
    link: HttpUrl

class LinkGet(BaseSchema):
    id: int
    original_link: str
    short_link: str

    model_config = ConfigDict(extra="ignore")