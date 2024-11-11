from fastapi import FastAPI

from src.api_v1 import router as api_v1_router
from src.settings import settings


app = FastAPI(title="Mospolytech DPO Parser")
app.include_router(api_v1_router)
