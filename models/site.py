from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base, session

class Site(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)
    size = Column(String)
    soil_type = Column(String)

    planters = relationship("Planter", back_populates="site")
    plants = relationship("Plant", back_populates="site")

    def __repr__(self):
        return f"<Site(id={self.id}, name='{self.name}', location='{self.location}')>"

    @classmethod
    def create(cls, name, location=None, size=None, soil_type=None):
        site = cls(name=name, location=location, size=size, soil_type=soil_type)
        session.add(site)
        session.commit()
        return site

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, site_id):
        return session.get(cls, site_id)

    def update(self, name=None, location=None, size=None, soil_type=None):
        if name: self.name = name
        if location: self.location = location
        if size: self.size = size
        if soil_type: self.soil_type = soil_type
        session.commit()
        return self

    def delete(self):
        session.delete(self)
        session.commit()
