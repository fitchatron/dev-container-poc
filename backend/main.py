from typing import Union

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import datetime
from pydantic import BaseModel
from models.user import Item
from db import db
app = FastAPI()

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

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/api/status")
def read_root():
    return {"Hello": datetime.datetime.now()}


@app.get("/api/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/api/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id < 0:
       raise HTTPException(status_code=404, detail="Item not found") 
    return {"item_name": item.name, "item_id": item_id}

@app.post("/api/items/", response_model=dict)
def create_item(name: str, price_in_cents: int):
    try:
        db_item = db.query(Item).filter(Item.name == name).first()
        if db_item:
            raise HTTPException(status_code=400, detail="Item already registered")
        new_item = Item(name=name, price_in_cents=price_in_cents, available=True)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return {"id": new_item.id, "price_in_cents": new_item.price_in_cents, "available": new_item.available}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating item: {e}")