from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base, session
import datetime

class Harvest(Base):
    __tablename__ = 'harvests'

    id = Column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey('plants.id'), nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String, default="kg")
    date = Column(Date, default=datetime.date.today)

    # Relationship with Plant
    plant = relationship("Plant", back_populates="harvests")

    def __repr__(self):
        return (
            f"<Harvest(id={self.id}, plant_id={self.plant_id}, "
            f"quantity={self.quantity}, unit='{self.unit}', date={self.date})>"
        )

    # -----------------------------
    # Class methods for CRUD
    # -----------------------------

    @classmethod
    def create(cls, plant_id, quantity, unit="kg", date=None):
        """Create a new Harvest record."""
        harvest = cls(
            plant_id=plant_id,
            quantity=quantity,
            unit=unit,
            date=date or datetime.date.today()
        )
        session.add(harvest)
        session.commit()
        return harvest

    @classmethod
    def get_all(cls):
        """Return all harvests."""
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, harvest_id):
        """Get a harvest by its ID."""
        return session.get(cls, harvest_id)

    # -----------------------------
    # Instance methods for update/delete
    # -----------------------------

    def update(self, quantity=None, unit=None, date=None):
        """Update harvest details."""
        if quantity is not None:
            self.quantity = float(quantity)
        if unit is not None:
            self.unit = unit
        if date is not None:
            self.date = date
        session.commit()
        return self

    def delete(self):
        """Delete the harvest record."""
        session.delete(self)
        session.commit()
