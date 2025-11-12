from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    category_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
        index=True
    )
    parent_category_id: Mapped[int | None] =  mapped_column(
        ForeignKey(
            "categories.id",
            ondelete="SET NULL",
        ),
        nullable=False
    )

    parent_category: Mapped["Category"] = relationship(
        "Category",
        remote_side=[id],
        back_populates="subcategories"
    )

    subcategories: Mapped[list["Category"]] = relationship(
        "Category",
        back_populates="parent_category",
        cascade="all",
        passive_deletes=True
    )

