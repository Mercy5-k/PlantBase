# This handles the database setup (the engine, session, and Base class)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create SQLite database
engine = create_engine("sqlite:///database/plantbase.db")

# This is the session that will be used to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# This is the base class for all our models
Base = declarative_base()


