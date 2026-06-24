from pydantic import BaseModel
from typing import Optional

# What the user sends to CREATE
# Student create -  is a schema for when someone wants to add a new student
class StudentCreate(BaseModel):
    name: str
    course: str
    grade: float = 0.0
    email: str


# what the user sends to UPDATE
# StudentUpdate - is for when someone wants to change a student's details
# The key difference is, here everything Optional. Why? everything is optional Because when updating 
# a user should be able to send just one field and change only that
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    course: Optional[str] = None
    grade: Optional[float] = None

# what the API sends back
# StudentResponse is what comes back when someone makes a request]
# notice the StudentResponse includes id (because after we create a student, we want 
# to tell the user what id they were assigned to)
class StudentResponse(BaseModel):
    id: int
    name: str
    course: str
    grade: float
    email: str

    # from_attributes = True is a bridge between the database world and API world
    # The database gives a SQLAlchemy object. The API needs to return Pydantic schema.
    class Config: # special class in pydantic ( it holds a configuraton settings)
        from_attributes = True # without this line. Pydantic cannot read SQLAlchemy model object
