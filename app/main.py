from fastapi import FastAPI
from app.routers import lead

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = FastAPI(title="LeadOnSpot AI Lead Qualification Agent")

app.include_router(lead.router)


@app.get("/")
def read_root():
    return {"message": "LeadOnSpot API is running"}