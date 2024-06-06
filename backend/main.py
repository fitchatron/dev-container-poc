from typing import Union

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import datetime
from pydantic import BaseModel
from models.user import User, Item, Order
from sqlalchemy.orm import Session
from db import get_db
app = FastAPI()

class POSTItem(BaseModel):
    name: str
    price_in_cents: int

class PUTItem(BaseModel):
    name: Union[str, None] = None
    price_in_cents: Union[int, None] = None
    available: Union[bool, None] = None


origins = [
    "http://localhost:3000",
    "http://172.19.0.3:3000/",
    "http://web:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/status")
def read_root():
    return {"Hello": datetime.datetime.now()}

@app.get("/api/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None, db: Session = Depends(get_db)):

    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {**db_item.as_dict(), "q": q}

@app.put("/api/items/{item_id}")
def update_item(item_id: int, item: PUTItem, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db_name_exists = db.query(Item).filter(Item.name == item.name).first()
    if db_name_exists and db_name_exists.id != item_id:
        raise HTTPException(status_code=400, detail="Item name already registered")
    
    db_item.name = item.name
    db_item.price_in_cents = item.price_in_cents
    db_item.available = item.available

    db.commit()
    db.refresh(db_item)
    return db_item.as_dict()

@app.post("/api/items/", response_model=dict)
def create_item(item: POSTItem, db: Session = Depends(get_db)):
    try:
        db_item = db.query(Item).filter(Item.name == item.name).first()
        if db_item:
            raise HTTPException(status_code=400, detail="Item already registered")
        new_item = Item(name=item.name, price_in_cents=item.price_in_cents, available=True)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item.as_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating item: {e}")