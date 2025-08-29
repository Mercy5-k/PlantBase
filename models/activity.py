from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base, session

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    plant_id = Column(Integer, ForeignKey("plants.id"))
    plant = relationship("Plant", back_populates="activities")

    def __repr__(self):
        return f"<Activity(id={self.id}, description='{self.description}', plant_id={self.plant_id}, timestamp={self.timestamp})>"

    @classmethod
    def create(cls, session, description, plant_id):
        activity = cls(description=description, plant_id=plant_id)
        session.add(activity)
        session.commit()
        return activity

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, session, activity_id):
        return session.get(cls, activity_id)

    def update(self, session, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                if key == "timestamp" and isinstance(value, str):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        session.commit()
        return self

    def delete(self, session):
        session.delete(self)
        session.commit()
