from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    is_ops_user: bool

    class Config:
        orm_mode = True

class FileBase(BaseModel):
    filename: str

class FileCreate(FileBase):
    pass

class File(FileBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
