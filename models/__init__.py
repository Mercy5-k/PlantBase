from .base import Base, engine, session
from .site import Site
from .planter import Planter
from .plant import Plant
from .harvest import Harvest
from .activity import Activity

# Safely create all tables if they don't exist
Base.metadata.create_all(engine)
