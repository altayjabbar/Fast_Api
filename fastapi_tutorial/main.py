from enum import Enum
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
