from models.user import User
from sqlalchemy.orm import Session
from dto.user import User as UserDTO

def create_user(data: UserDTO, db: Session):
    user = User(**data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(id: int, db: Session):
    return db.query(User).filter(User.id == id).first()

def update_user(id: int, data: UserDTO, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if user:
        if data.name is not None:
            user.name = data.name
        if data.email is not None:
            user.email = data.email
        if data.age is not None:
            user.age = data.age
        if data.is_active is not None:
            user.is_active = data.is_active
        if data.registration_date is not None:
            user.registration_date = data.registration_date
        db.commit()
        db.refresh(user)
    return user

def delete_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"message": "User deleted successfully"}
    return {"message": "User not found"}
