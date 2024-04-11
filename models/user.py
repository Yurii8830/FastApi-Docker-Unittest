from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from database import Base
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
    active = Column(Boolean, default=True)
    registration_date = Column(Date)

    # Встановлення взаємодії з класом Record
    records = relationship("Record", back_populates="user", cascade="all, delete-orphan")