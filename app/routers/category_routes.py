# app/api/v1/category_routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.services.category import CategoryService
from app.schemas.category import (
    CategoryRead,
    CategoryCreate,
    CategoryUpdate,
)

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=list[CategoryRead])
async def get_categories(db: AsyncSession = Depends(get_db)):
    return await CategoryService.get_all(db)


@router.get("/{category_id}", response_model=CategoryRead)
async def get_category(category_id: int, db: AsyncSession = Depends(get_db)):
    return await CategoryService.get_by_id(category_id, db)


@router.post("/", response_model=CategoryRead, status_code=201)
async def create_category(
    data: CategoryCreate,
    db: AsyncSession = Depends(get_db)
):
    return await CategoryService.create(data, db)


@router.patch("/{category_id}", response_model=CategoryRead)
async def update_category(
    category_id: int,
    data: CategoryUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await CategoryService.update(category_id, data, db)


@router.delete("/{category_id}", status_code=204)
async def delete_category(
    category_id: int,
    db: AsyncSession = Depends(get_db),
):
    await CategoryService.delete(category_id, db)
    return {"message": "Deleted"}
