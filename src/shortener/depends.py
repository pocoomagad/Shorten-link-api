from fastapi import Depends

from typing import Annotated

from src.shortener.service import UrlShortenerService

def get_url_shortener_service() -> UrlShortenerService:
    return UrlShortenerService()

UrlShortenerServiceDep = Annotated[UrlShortenerService, Depends(get_url_shortener_service)]