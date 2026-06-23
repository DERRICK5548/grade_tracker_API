from sqlalchemy import Column, Integer, String, Float # This is how we define a column inside our table
from database import Base # we import Base from own database.py file inherit the parent class

class Students(Base): # this create a python class called Student. By inheriting from the base
    __tablename__="Students" # table name

    id = Column(Integer, primary_key=True, index=True)# id is a column in integer and its unique
    name = Column(String, nullable=False) # nullable = False means that this field is required
    course = Column(String, nullable=False)
    grade = Column(Float, default=0.0)# grade is a column, and the data type is float, incase of no data it's default is 0
    email = Column(String, unique=True)