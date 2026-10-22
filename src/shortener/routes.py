from fastapi import APIRouter, status, Path
from fastapi.responses import RedirectResponse

from src.shortener.schemas import LinkGet, LinkDTO
from src.shortener.depends import UrlShortenerServiceDep

shortener_router = APIRouter(
    prefix="/"
)

@shortener_router.post(
    "/shorten",
    status_code=status.HTTP_201_CREATED
)
async def shortener_link(
    url: LinkDTO,
    service: UrlShortenerServiceDep
) -> LinkGet:
    return await service.add_short_link(url.link)

@shortener_router.post(
    "{short_code}",
    status_code=status.HTTP_301_MOVED_PERMANENTLY
)
async def move_by_short_code(
    short_code: str,
    service: UrlShortenerServiceDep
) -> RedirectResponse:
    response_link = await service.get_original_link_by_short_code(short_code)
    return RedirectResponse(url=response_link, status_code=status.HTTP_301_MOVED_PERMANENTLY)