from typing import List, ClassVar

from fastapi import FastAPI, HTTPException, Query, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    text: str = None
    is_there: bool = False


items = []


@app.get("/")
def root():
    return {"Hello, Beautiful World"}


@app.post("/item")
def post_an_item(item: List[Item] = Body([])):
    items.extend(item)
    return items


@app.get("/items")
def get_all_items():
    return items


@app.get("/items/{item_id}", response_model=Item)
def get_a_single(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]

    else:
        raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")


@app.get("/items")
def get_a_multiple(something: int = 10):
    return items[0:something]
