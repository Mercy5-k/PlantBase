from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base, session

class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String)
    age_months = Column(Integer)
    health_status = Column(String)

    site_id = Column(Integer, ForeignKey("sites.id"))
    planter_id = Column(Integer, ForeignKey("planters.id"))

    site = relationship("Site", back_populates="plants")
    planter = relationship("Planter", back_populates="plants")
    harvests = relationship("Harvest", back_populates="plant")
    activities = relationship("Activity", back_populates="plant")

    def __repr__(self):
        return f"<Plant(id={self.id}, name='{self.name}')>"

    @classmethod
    def create(cls, name, site_id, planter_id, **kwargs):
        plant = cls(name=name, site_id=site_id, planter_id=planter_id, **kwargs)
        session.add(plant)
        session.commit()
        return plant

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, plant_id):
        return session.get(cls, plant_id)

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        session.commit()
        return self

    def delete(self):
        session.delete(self)
        session.commit()
