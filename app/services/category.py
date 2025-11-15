from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.category import CategoryRepository
from app.schemas.category import CategoryCreate, CategoryUpdate
from app.models.category import Category


class CategoryService:

    @staticmethod
    async def get_all(db: AsyncSession):
        return await CategoryRepository.get_all(db)

    @staticmethod
    async def get_by_id(category_id: int, db: AsyncSession):
        category = await CategoryRepository.get_by_id(db, category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found"
            )
        return category

    @staticmethod
    async def create(data: CategoryCreate, db: AsyncSession):
        if data.parent_category_id:
            parent = await CategoryRepository.get_by_id(
                db, data.parent_category_id
            )

            if not parent:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Parent category not found"
                )
        new_category = Category(
            category_name = data.category_name,
            category_parent_id = data.parent_category_id,
        )

        return await CategoryRepository.create(db, new_category)

    @staticmethod
    async def update(category_id: int, data: CategoryUpdate, db: AsyncSession):
        category = await CategoryRepository.get_by_id(db, category_id)
        if data.category_name is not None:
            category.category_name = data.category_name

        if data.parent_category_id is not None:
            if data.parent_category_id == category.id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Category cannot be parent of itself."
                )
            category.category_parent_id = data.parent_category_id

        await CategoryRepository.update(db)
        return category

    @staticmethod
    async def delete(category_id: int, db: AsyncSession):
        category = await CategoryService.get_by_id(category_id, db)
        await CategoryRepository.delete(db, category)
        return True


