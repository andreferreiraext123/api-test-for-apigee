"""Main"""

from fastapi import FastAPI
from app.routers import fuel
from app.cache.cache import fuels

app = FastAPI(title="GA Balance", version="1.0.0")

app.include_router(fuel.router)

@app.get("/")
def heath_check():
    """Health check endpoint"""
    return {"status": "ok"}
