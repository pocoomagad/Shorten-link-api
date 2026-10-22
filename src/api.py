#все эндпоинты в одном файле

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.shortener.routes import shortener_router
from src.statistics.routes import statistic_router

api_router = APIRouter(prefix="/api")

api_router.include_router(shortener_router)
api_router.include_router(statistic_router)

@api_router.get(
    "/health",
    status_code=status.HTTP_200_OK
)
async def get_health() -> JSONResponse:
    return JSONResponse(
        {
            "api": "ok"
        }
    )