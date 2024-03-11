# schemas.py
from pydantic import BaseModel

class BondCreate(BaseModel):
    price: str
    single: str
    multiple: str
    start: str
    end: str

class BondUpdate(BaseModel):
    price: str
    single: str
    multiple: str
    start: str
    end: str

class BondResponse(BaseModel):
    id: int
    price: str
    single: str
    multiple: str
    start: str
    end: str

    class Config:
        from_attributes = True
