from enum import Enum
from typing import Optional
from fastapi import FastAPI  # type: ignore

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/")
async def post():
    return {"message": "hello by post owner"}


@app.put("/")
async def post():
    return {"message": "put fist post"}


@app.delete("/")
async def delete():
    return {"message": "delete all post"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):

    if food_name == FoodEnum.fruits:
        return {"food_name": food_name, "message": "you are healthy"}

    if food_name.value == "fruits":
        return {"food_name": food_name, "message": "this fantastic"}

    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "this is natural"}

    if food_name == FoodEnum.dairy:
        return {"food_name": food_name, "message": "this is natural"}
    return {"food_name": "food_name", "message": "this is perfect competetion"}

fake_db = [{"item_name":"bob"},{"item_name":"Ricard"},{"item_name":"bow"}]
# query parametr
@app.get("/items")
async def  list_items(skip: int = 0, limit: int = 10):
    return fake_db[skip: skip + limit]

@app.get("/items/{item_id}")
async def get_item(item_id: str, q: str|None =None, short: bool = False):
    item = {"item_id":item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"nothing "})    
    return item

@app.get("/users/{users_id}/items/{items_id}")
async def get_user_item(user_id:int, item_id:int, q: str|None = None, short:bool = False):
    item = {"item_id":item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":'nothing'})
    return item 