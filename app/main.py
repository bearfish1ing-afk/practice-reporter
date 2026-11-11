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
