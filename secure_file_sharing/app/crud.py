from sqlalchemy.orm import Session
from app import models, schemas
from app.security import get_password_hash

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_file(db: Session, file: schemas.FileCreate, user_id: int):
    db_file = models.File(**file.dict(), owner_id=user_id)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

def get_files(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.File).offset(skip).limit(limit).all()
