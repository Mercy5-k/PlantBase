from .base import Base, engine
from .planter import Planter

# Create all tables in the database
Base.metadata.create_all(engine)