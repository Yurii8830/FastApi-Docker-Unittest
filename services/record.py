from models.record import Record
from sqlalchemy.orm import Session
from dto.record import Record as RecordDTO
from fastapi import Depends
from database import get_db
from dto import record as RecordDTO
from models.user import User

def create_record(user, data: RecordDTO.Record = None, db: Session = Depends(get_db)):
    record = Record(title=data.title, content=data.content, user_id=user.id, date=data.date)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_record(id: int, db: Session):
    return db.query(Record).filter(Record.id == id).first()

def update_record(id: int, data: RecordDTO, db: Session):
    record = db.query(Record).filter(Record.id == id).first()
    if record:
        if data.title is not None:
            record.title = data.title
        if data.content is not None:
            record.content = data.content
        if data.user_id is not None:
            record.user_id = data.user_id
        if data.date is not None:
            record.date = data.date
        db.commit()
        db.refresh(record)
    return record

def delete_record(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return False
    # Видалення всіх записів, які належать користувачеві
    db.query(Record).filter(Record.user_id == user.id).delete()
    db.delete(user)
    db.commit()
    return True
