from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    category_name: str
    parent_category_id: int | None = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    category_name: str | None = None
    parent_category_id: int | None = None


class CategoryRead(CategoryBase):
    id: int
    subcategories: list["CategoryRead"] = Field(default_factory=list)

    class Config:
        orm_mode = True

CategoryRead.model_rebuild()




