from abc import ABC, abstractmethod

from sqlalchemy import select

from src.database.models import LinkLogModel, LinkModel
from src.database.config import Session

from src.statistics.schemas import StatisticsLinkSchema

class AbstractLinkLogService(ABC):
    @abstractmethod
    async def get_logs_by_id(self, id: int) -> list:
        ...

class LinkLogService(AbstractLinkLogService):
    async def get_logs_by_id(self, id: int):
        async with Session() as session:
            get_logs = (
                select(LinkLogModel, LinkModel.creation_date)
                .filter_by(id=id)
                .join(LinkModel)
            )

            log_model = await session.execute(get_logs)
            await session.commit()
            return StatisticsLinkSchema.model_dump(log_model.scalars().all())