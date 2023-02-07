from shop.database import Base
from sqlalchemy import Column, String, Integer, Text


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    description = Column(Text)
