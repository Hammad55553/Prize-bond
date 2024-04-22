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

class AccountCreate(BaseModel):
    email: str
    password: str
    fullName: str
    phoneNumber: str

class AccountUpdate(BaseModel):
    password: str
    fullName: str
    phoneNumber: str

class AccountResponse(BaseModel):
    id: int
    email: str
    password: str


    class Config:
        from_attributes = True
