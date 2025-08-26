from sqlalchemy import Column, Integer, String
from .base import Base

class Planter(Base):
    __tablename__ = 'planters'

    # the table columns 
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)
    contact_info = Column(String)

    def __repr__(self):
        """String representation which is readable and useful for debugging."""
        return f"<Planter(id={self.id}, name={self.name}, ({self.contact_info})>"