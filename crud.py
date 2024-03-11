# crud.py
from sqlalchemy.orm import Session
from models import Bond
from schemas import BondCreate, BondUpdate

def create_bond(db: Session, bond: BondCreate):
    db_bond = Bond(**bond.dict())
    db.add(db_bond)
    db.commit()
    db.refresh(db_bond)
    return db_bond

def read_bond(db: Session, bond_id: int):
    return db.query(Bond).filter(Bond.id == bond_id).first()

def update_bond(db: Session, bond_id: int, bond_update: BondUpdate):
    db_bond = db.query(Bond).filter(Bond.id == bond_id).first()
    for key, value in bond_update.dict().items():
        setattr(db_bond, key, value)
    db.commit()
    db.refresh(db_bond)
    return db_bond

def delete_bond(db: Session, bond_id: int):
    db_bond = db.query(Bond).filter(Bond.id == bond_id).first()
    db.delete(db_bond)
    db.commit()

def read_bonds(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Bond).offset(skip).limit(limit).all()
