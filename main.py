from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="My API")

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = 0.0

items_db: List[Item] = []

@app.get("/")
def root():
    return {
        "message": "Добро пожаловать в API детских товаров!",
        "docs": "/docs",
        "items": "/items/"
    }

@app.get("/items/", response_model=List[Item])
def get_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    for existing in items_db:
        if existing.id == item.id:
            raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items_db.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            updated_item.id = item_id
            items_db[idx] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            deleted = items_db.pop(idx)
            return {"message": f"Item '{deleted.name}' deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/")
def clear_items():
    count = len(items_db)
    items_db.clear()
    return {"message": f"Deleted {count} items"}


