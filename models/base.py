import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database path
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "plantbase.db")
DB_PATH = os.path.abspath(DB_PATH)

# Engine and session
engine = create_engine(f"sqlite:///plantbase.db", echo=False)  # echo=True for debug

Session = sessionmaker(bind=engine)
session = Session()

# Base declarative class
Base = declarative_base()
