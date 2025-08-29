import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "plantbase.db")
DB_PATH = os.path.abspath(DB_PATH)

engine = create_engine(f"sqlite:///plantbase.db", echo=False) 

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
