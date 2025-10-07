"""Fuel Models"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from decimal import Decimal

class Fuel(BaseModel):
    """Base Model for Fuel"""
    name: str = Field(..., example="Diesel")
    id: str = Field(..., example="123")
    price_per_liter: float = Field(..., example=1.23)
    station_id: int = Field(..., example= 12321)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class FuelCreate(Fuel):
    """Model for creating Fuel"""

class FuelUpdate(BaseModel):
    """Model for updating Fuel"""
    name: Optional[str] = Field(..., example="Diesel")
    price_per_liter: Optional[float] = Field(..., example=1.23)