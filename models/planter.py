from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .base import Base

class Planter(Base):
    __tablename__ = 'planters'

    # The table columns 
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)

    # Fields for the planters 
    plant_type = Column(String, nullable=True)
    experience_level = Column(String, nullable=True)
    experience_months = Column(Integer, default=0)
    farm_size = Column (String)
    preferred_tools =Column(String)

    created_at = Column(DateTime, default=datetime.now)  # Records the time it was created

    def __repr__(self):
        """String representation which is readable and useful for debugging."""
        return (
        f"<Planter {self.name} | {self.plant_type} | "
        f"Exp: {self.experience_level} ({self.experience_months} months)>"
        )