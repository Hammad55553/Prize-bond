from sqlalchemy.orm import Session
from models import Bond, Signup
from schemas import BondCreate, BondUpdate, AccountCreate, AccountUpdate

# CRUD operations for Bond model
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

# CRUD operations for Signup model
def create_account(db: Session, account: AccountCreate):
    db_account = Signup(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def read_account(db: Session, email: str):
    return db.query(Signup).filter(Signup.email == email).first()
def update_account(db: Session, email: str, account_update: AccountUpdate):
    db_account = db.query(Signup).filter(Signup.email == email).first()
    for key, value in account_update.dict().items():
        setattr(db_account, key, value)
    db.commit()
    db.refresh(db_account)
    return db_account

def delete_account(db: Session, email: str):
    db_account = db.query(Signup).filter(Signup.email == email).first()
    db.delete(db_account)
    db.commit()

def read_accounts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Signup).offset(skip).limit(limit).all()
