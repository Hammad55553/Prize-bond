from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import crud, models, schemas
from database import engine, SessionLocal

app = FastAPI()

# CORS Configuration for local development
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/bond/", response_model=schemas.BondResponse)
def create_bond(bond: schemas.BondCreate, db: Session = Depends(get_db)):
    return crud.create_bond(db, bond)

@app.get("/bond/{bond_id}", response_model=schemas.BondResponse)
def read_bond(bond_id: int, db: Session = Depends(get_db)):
    db_bond = crud.read_bond(db, bond_id)
    if db_bond is None:
        raise HTTPException(status_code=404, detail="Bond not found")
    return db_bond

@app.put("/bond/{bond_id}", response_model=schemas.BondResponse)
def update_bond(bond_id: int, bond_update: schemas.BondUpdate, db: Session = Depends(get_db)):
    db_bond = crud.update_bond(db, bond_id, bond_update)
    if db_bond is None:
        raise HTTPException(status_code=404, detail="Bond not found")
    return db_bond

@app.delete("/bond/{bond_id}", response_model=schemas.BondResponse)
def delete_bond(bond_id: int, db: Session = Depends(get_db)):
    db_bond = crud.delete_bond(db, bond_id)
    if db_bond is None:
        raise HTTPException(status_code=404, detail="Bond not found")
    return db_bond

@app.get("/bonds/", response_model=list[schemas.BondResponse])
def read_bonds(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.read_bonds(db, skip=skip, limit=limit)

@app.post("/signup/", response_model=schemas.AccountResponse)
def create_account(account: schemas.AccountCreate, db: Session = Depends(get_db)):
    return crud.create_account(db, account)

@app.get("/signup/{email}/{password}", response_model=schemas.AccountResponse)
def read_account(email: str, password: str, db: Session = Depends(get_db)):
    db_account = crud.read_account(db, email)
    if db_account is None or db_account.password != password:
        raise HTTPException(status_code=404, detail="Account not found or incorrect password")
    return db_account

@app.put("/signup/{email}", response_model=schemas.AccountResponse)
def update_account(email: str, account_update: schemas.AccountUpdate, db: Session = Depends(get_db)):
    db_account = crud.update_account(db, email, account_update)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@app.delete("/signup/{email}", response_model=schemas.AccountResponse)
def delete_account(email: str, db: Session = Depends(get_db)):
    db_account = crud.delete_account(db, email)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@app.get("/signups/", response_model=list[schemas.AccountResponse])
def read_accounts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.read_accounts(db, skip=skip, limit=limit)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="192.162.0.1", port=8000)
