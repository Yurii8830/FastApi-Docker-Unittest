from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from services import user as UserService
from dto import user as UserDTO
from services import record as RecordService
from dto import record as RecordDTO

router = APIRouter()

@router.post('/user', tags=["user"])
def create_user(data: UserDTO.User = None, db: Session = Depends(get_db)):
    return UserService.create_user(data, db)

@router.get('/user/{id}', tags=["user"])
def get_user(id: int, db: Session = Depends(get_db)):
    return UserService.get_user(id, db)

@router.put('/user/{id}', tags=["user"])
def update_user(id: int, data: UserDTO.User = None, db: Session = Depends(get_db)):
    if not UserService.get_user(id, db):
        return {"message": "User not found"}
    return UserService.update_user(id, data, db)

@router.delete('/user/{id}', tags=["user"])
def delete_user(id: int, db: Session = Depends(get_db)):
    if not UserService.get_user(id, db):
        return {"message": "User not found"}
    return UserService.delete_user(id, db)

@router.post('/record', tags=["record"])
def create_record(user_id: int, data: RecordDTO.Record = None, db: Session = Depends(get_db)):
    user = UserService.get_user(user_id, db)
    if not user:
        return {"message": "User not found"}
    return RecordService.create_record(user, data, db)


@router.get('/record/{id}', tags=["record"])
def get_record(id: int, db: Session = Depends(get_db)):
    return RecordService.get_record(id, db)

@router.put('/record/{id}', tags=["record"])
def update_record(id: int, data: RecordDTO.Record = None, db: Session = Depends(get_db)):
    if not RecordService.get_record(id, db):
        return {"message": "Record not found"}
    return RecordService.update_record(id, data, db)

@router.delete('/record/{id}', tags=["record"])
def delete_record(id: int, db: Session = Depends(get_db)):
    record = RecordService.get_record(id, db)
    if not record:
        return {"message": "Record not found"}
    db.delete(record)
    db.commit()
    return {"message": "Record deleted successfully"}
