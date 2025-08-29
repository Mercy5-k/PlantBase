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

    plant = relationship("Plant", back_populates="harvests")

    def __repr__(self):
        return f"<Harvest(id={self.id}, plant_id={self.plant_id}, quantity={self.quantity}, unit='{self.unit}', date={self.date})>"

    @classmethod
    def create(cls, plant_id, quantity, unit="kg", date=None):
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
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, harvest_id):
        return session.get(cls, harvest_id)

    def update(self, quantity=None, unit=None, date=None):
        if quantity is not None:
            self.quantity = float(quantity)
        if unit is not None:
            self.unit = unit
        if date is not None:
            if isinstance(date, str):
                self.date = datetime.datetime.fromisoformat(date).date()
            elif isinstance(date, datetime.date):
                self.date = date
        session.commit()
        return self

    def delete(self):
        session.delete(self)
        session.commit()
