from fastapi import FastAPI
import uvicorn

from src.api import api_router

app = FastAPI()

# app.include_router(api_router)