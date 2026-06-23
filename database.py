from sqlalchemy import create_engine # create engine is a function that creates the connection
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker # a function that produces database sessions on demand

DATABASE_URL = "sqlite:///./grades.db" # This string tells the SQLAlchemy where exactly our database lives -> "./" the same folder

# the engine is the actual connection to the database. It uses the URL to know where to connect
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread: False"})

# SessionLocal - blueprint for creating session
SessionLocal = sessionmaker(autoflush=False, autocomit=False, bind =engine)

# Base is the parent class for all our database models. class Student(Base)
# SQLAlchemy knows Student is database table
Base = declarative_base()

def get_db():
    db = SessionLocal() # creates a fresh database session

    try: 
        yield db # yield gives the session to whoever called get_db and PAUSES here
    finally:
        db.close() # closes the session and returns the connection. Cleanup happens   