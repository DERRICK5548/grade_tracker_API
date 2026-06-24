from sqlalchemy.orm import Session  
import models, schemas

# CREATE
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Students(**student.model_dump())
    db.add(db_student) # stage the recordl Tells SQLAlchemy 'I want to save this'
    db.commit() # Save to disk. This when the data is actually written to database
    db.refresh(db_student) # reloads the object from databasr after saving, (new_id)
    return db_student # return completed student object

# READ one record
def get_student(db: Session, student_id: int):
    return db.query(models.Students).filter(models.Students.id == student_id).first()

# READ ALL record
def get_students(db: Session):
    return db.query(models.Students).all()

# UPDATE a record
def update_student(db: Session, student_id: int, data: schemas.StudentUpdate):
    student= db.query(models.Students).filter(models.Students.id == student_id).first() # finding the student
    if not student: # if there is no student with that id, it returns None
        return None
    updates = data.model_dump(exclude_unset=True) # converts the update data to a dictionary(
    # e.g if the user only set grade, updates will only contain grade)
    for field, value in updates.items(): # Loop through each field and value that was sent
        setattr(student, field, value) #sets an attribute on an object by name

    db.commit()
    db.refresh(student)
    return student

# DELETE/REMOVE
def delete_student(db: Session, student_id: int):
    # Find the student first-> You cannot delete something you have not found
    student = db.query(models.Students).filter(models.Students.id == student_id).first()
    if not student: # If not found-> return None
        return None
    db.delete(student)
    db.commit()
    return student