from fastapi import Depends
from typing import Annotated

from src.statistics.service import LinkLogService

def get_link_log_service() -> LinkLogService:
    return LinkLogService()

LinkLogServiceDep = Annotated[LinkLogService, Depends(get_link_log_service)]