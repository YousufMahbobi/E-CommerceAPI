from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.category import Category

class CategoryRepository:

    @staticmethod
    async def get_all(db: AsyncSession):
        stmt = (
                   select(Category)
                   .where(Category.parent_category_id.is_(None))
                   .order_by(Category.category_name)
               )
        result = await db.execute(stmt)
        return result.scalars().unique().all()


    @staticmethod
    async def get_by_id(db: AsyncSession, category_id: int):
        stmt = select(Category).where(Category.id == category_id)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()


    @staticmethod
    async def create(db: AsyncSession, category: Category):
        db.add(category)
        await db.commit()
        await db.refresh(category)
        return category


    @staticmethod
    async def delete(db: AsyncSession, category: Category):
        await db.delete(category)
        await db.commit()


    @staticmethod
    async def update(db: AsyncSession):
        await db.commit()


