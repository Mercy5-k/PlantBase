from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base, session

class Planter(Base):
    __tablename__ = "planters"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)
    contact_info = Column(String)
    plant_type = Column(String)
    experience_level = Column(String)
    experience_months = Column(Integer)
    farm_size = Column(String)
    preferred_tools = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    site_id = Column(Integer, ForeignKey("sites.id"), nullable=True)
    site = relationship("Site", back_populates="planters")

    plants = relationship("Plant", back_populates="planter")

    def __repr__(self):
        return f"<Planter(id={self.id}, name='{self.name}')>"

    @classmethod
    def create(cls, name, site_id=None, **kwargs):
        """Create a new planter and save to DB."""
        planter = cls(name=name, site_id=site_id, **kwargs)
        session.add(planter)
        session.commit()
        return planter

    @classmethod
    def get_all(cls):
        """Return all planters."""
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, planter_id):
        """Return a planter by ID."""
        return session.get(cls, planter_id)

    def update(self, **kwargs):
        """Update planter attributes and commit."""
        for k, v in kwargs.items():
            setattr(self, k, v)
        session.commit()
        return self

    def delete(self):
        """Delete planter from the database."""
        session.delete(self)
        session.commit()
