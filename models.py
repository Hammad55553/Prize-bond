# models.py
from sqlalchemy import Column, Integer, String
from database import Base

class Bond(Base):
    __tablename__ = "add_bond"
    id = Column(Integer, primary_key=True, index=True)
    price = Column(String, index=True)
    single = Column(String)
    multiple = Column(String)
    start = Column(String)
    end = Column(String)

class Signup(Base):
    __tablename__ = "sign_up"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    fullName = Column(String)
    phoneNumber = Column(String)
       
