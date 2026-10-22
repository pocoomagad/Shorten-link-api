from fastapi import APIRouter, status

from src.statistics.schemas import StatisticsLinkSchema
from src.statistics.depends import LinkLogServiceDep

statistic_router = APIRouter(
    prefix="/logs"
)

@statistic_router.get(
    "",
    status_code=status.HTTP_200_OK
)
async def get_all_logs(
    id: int,
    service: LinkLogServiceDep
) -> StatisticsLinkSchema:
    return await service.get_logs_by_id(id)