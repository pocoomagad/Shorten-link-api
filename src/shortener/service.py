from abc import ABC, abstractmethod

from sqlalchemy import insert, update, select

from typing import Any

from src.database.config import Session
from src.database.models import LinkModel
from src.shortener.flows import encode, decode

class AbstractUrlShortenerService(ABC):
    @abstractmethod
    async def add_short_link(self, url: str) -> list[Any]:
        raise NotImplementedError

    @abstractmethod
    async def get_original_link_by_short_code(self, short_code: str) -> str:
        raise NotImplementedError

class UrlShortenerService(AbstractUrlShortenerService):
    async def add_short_link(self, url: str) -> list[LinkModel]:
        async with Session() as session:
            add_and_return_id = (
                insert(LinkModel)
                .values(LinkModel.original_link==url, LinkModel.short_link==None)
                .returning(LinkModel.id)
            )

            id = await session.execute(add_and_return_id)

            short_code = encode(id.scalar())
            short_link = "path{0}{1}".format("/", short_code)

            add_short_link = (
                update(LinkModel)
                .values(LinkModel.short_link==short_link)
                .returning(
                    LinkModel.id, 
                    LinkModel.original_link, 
                    LinkModel.short_link, 
                    LinkModel.creation_date
                    )
            )

            record_link = await session.execute(add_short_link)
            await session.commit()
            return record_link.scalars().all()

    async def get_original_link_by_short_code(self, short_code: str) -> str:
        id = decode(short_code)

        async with Session() as session:
            get_original_link = (
                select(LinkModel.original_link)
                .filter_by(id=id)
            )

            original_link = await session.execute(get_original_link)
            await session.commit()
            return original_link.scalar()