from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime, ForeignKey

from datetime import timezone


class Base(DeclarativeBase):
    def __repr__(self):
        return 


class LinkModel(Base):

    __tablename__ = "links"

    id: Mapped[int] = mapped_column(primary_key=True)
    original_link: Mapped[str] = mapped_column(nullable=False, unique=False)
    short_link: Mapped[str] = mapped_column(nullable=True)
    creation_date: Mapped[DateTime] = mapped_column(DateTime(timezone.utc))

class LinkLogModel(Base):

    __tablename__ = ""

    id: Mapped[int] = mapped_column(ForeignKey("short_url.id"))
    time_click: Mapped[DateTime] = mapped_column(DateTime(timezone.utc))
