from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(title="연습 API")

class Item(BaseModel):
  name:str
  price:int

@app.get("/items")
def list_items():
  return []

@app.post("/items")
def create_item(item: Item):
  return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
  return {"delete":item_id}

@app.get("/items/{item_id}")
def get_item(item_id: int):
  return {"id": item_id}
