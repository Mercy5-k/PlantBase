from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .base import Base, session

class Planter(Base):
    __tablename__ = 'planters'

    # The table columns 
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
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
    
    # Inserting CRUD Methods 
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def get_by_id(cls, planter_id):
        return session.query(cls).filter_by(id=planter_id).first()
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()