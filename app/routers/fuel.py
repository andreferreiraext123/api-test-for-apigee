"""Fuel Routes"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.fuel import FuelCreate, FuelUpdate
from app.cache.cache import fuels
from datetime import datetime

router = APIRouter(prefix = "/fuels", tags = ["Fuels"])


@router.get("/")
async def get_fuel():
    return {
        "Fuel Kinds": fuels
    }

@router.get("/{fuel_id}")
async def get_fuel_by_id(fuel_id: str):
    for fuel in fuels:
        if fuel_id is fuel.id:
            return {"Found": fuel}

    raise HTTPException(
        status_code=404, detail="Fuel not found")

@router.post("/")
async def create_fuel(fuel: FuelCreate):
    fuels.append(fuel)
    return {
        "Received": fuel
    }

@router.patch("/{fuel_id}")
async def update_fuel(fuelUp: FuelUpdate, fuel_id: str):
    for fuel in fuels:
        if fuel_id is fuel.id:
            if fuelUp.name is not None:
                fuel.name = fuelUp.name
            if fuelUp.price_per_liter is not None:
                fuel.price_per_liter = fuelUp.price_per_liter
            fuel.updated_at = datetime.now()
            return {
                "Updated": f"Fuel {fuel_id} updated successfully"
            }
    raise HTTPException(
        status_code=404, detail="Fuel not found"
    )

@router.delete("/{fuel_id}")
async def delete_fuel_by_id(fuel_id: str):
    for index, fuel in enumerate(fuels):
        if fuel_id is fuel.id:
            del fuels[index]
            return {
                f"Fuel deleted id: {fuel_id}"
            }
    raise HTTPException(
        status_code=404, detail="Fuel not found"
    )