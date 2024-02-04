from typing import List

from sqlalchemy.orm import Mapped, relationship

from src.database.models.characteristics.base import AbstractCharacteristicModel


class Country(AbstractCharacteristicModel):
    __tablename__ = "country"

    addresses: Mapped[List["Address"]] = relationship(back_populates="country", uselist=True)

    def __repr__(self) -> str:
        return f"Country(id={self.id}, title={self.title})"
