from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

class DeckOut(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True
