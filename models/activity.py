from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base, session

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)  # Use UTC to avoid timezone issues

    plant_id = Column(Integer, ForeignKey("plants.id"))
    plant = relationship("Plant", back_populates="activities")

    def __repr__(self):
        return f"<Activity(id={self.id}, description='{self.description}', plant_id={self.plant_id}, timestamp={self.timestamp})>"

    @classmethod
    def create(cls, session, description, plant_id):
        """Create a new activity linked to a plant"""
        activity = cls(description=description, plant_id=plant_id)
        session.add(activity)
        session.commit()
        return activity

    @classmethod
    def get_all(cls, session):
        """Return all activities"""
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, session, activity_id):
        """Return an activity by ID"""
        return session.get(cls, activity_id)

    def update(self, session, description=None):
        """Update the description of the activity"""
        if description:
            self.description = description
        session.commit()
        return self

    def delete(self, session):
        """Delete this activity"""
        session.delete(self)
        session.commit()
