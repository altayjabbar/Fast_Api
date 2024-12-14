from enum import Enum
from uuid import UUID
from datetime import datetime
from typing import Optional, List
from fastapi import Body, FastAPI, Query, Path, Cookie, Header, Form # type: ignore
from pydantic import BaseModel, Field, EmailStr  # type: ignore

app = FastAPI()


# # @app.get("/")
# # async def root():
# #     return {"message": "hello world"}


# # @app.post("/")
# # async def post():
# #     return {"message": "hello by post owner"}


# # @app.put("/")
# # async def post():
# #     return {"message": "put fist post"}


# # @app.delete("/")
# # async def delete():
# #     return {"message": "delete all post"}


# # class FoodEnum(str, Enum):
# #     fruits = "fruits"
# #     vegetables = "vegetables"
# #     dairy = "dairy"


# # @app.get("/foods/{food_name}")
# # async def get_food(food_name: FoodEnum):

# #     if food_name == FoodEnum.fruits:
# #         return {"food_name": food_name, "message": "you are healthy"}

# #     if food_name.value == "fruits":
# #         return {"food_name": food_name, "message": "this fantastic"}

# #     if food_name == FoodEnum.vegetables:
# #         return {"food_name": food_name, "message": "this is natural"}

# #     if food_name == FoodEnum.dairy:
# #         return {"food_name": food_name, "message": "this is natural"}
# #     return {"food_name": "food_name", "message": "this is perfect competetion"}

# # fake_db = [{"item_name":"bob"},{"item_name":"Ricard"},{"item_name":"bow"}]
# # # query parametr
# # @app.get("/items")
# # async def  list_items(skip: int = 0, limit: int = 10):
# #     return fake_db[skip: skip + limit]

# # @app.get("/items/{item_id}")
# # async def get_item(item_id: str, q: str|None =None, short: bool = False):
# #     item = {"item_id":item_id}
# #     if q:
# #         item.update({"q":q})
# #     if not short:
# #         item.update({"description":"nothing "})
# #     return item

# # @app.get("/users/{users_id}/items/{items_id}")
# # async def get_user_item(user_id:int, item_id:int, q: str|None = None, short:bool = False):
# #     item = {"item_id":item_id}
# #     if q:
# #         item.update({"q":q})
# #     if not short:
# #         item.update({"description":'nothing'})
# #     return item


# # class Item(BaseModel):
# #     name: str
# #     descreption: str | None = None
# #     price: float
# #     tax : float | None = None

# # @app.post("/items")
# # async def  create_item(item:Item):
# #     item_dict = item.dict()
# #     if item.tax:
# #         price_with_tax = item.price + item.tax
# #         item_dict.update({"price_with_tax":price_with_tax})
# #     return item_dict

# # @app.put("/items/{item_id}")
# # async def create_item_with_put(item_id: int,item:Item,q: str|None = None):
# #     result = {"item_id":item_id,**item.dict()}
# #     if q:
# #         result.update({"q":q})
# #     return result

# # class Transport(BaseModel):
# #     color: str
# #     value : float
# #     description: str|None = None

# # @app.post("/transport")
# # async def transport(transport:Transport):
# #     return transport


# # @app.get("/itemss")
# # async def items(q: str = Query("altayjabbar", min_length=3, max_length=10, regex="^altayjabbar$", alias="txt")):
# #     results = {"items": [{"item_id": "Foo"}, {"item_id": "bar"}]}
# #     results.update({"q": q})
# #     return results


# # @app.get("/items_validations{itemdsd_id}")
# # async def read_items_validation(
# #     itemdsd_id: int = Path(..., title="Item id"),
# #     q: str | None = Query(None, alias='item-query'),
# #     size: float = Query(..., gt =1, lt = 10)
# # ):
# #     results = {"itemdsd_id": itemdsd_id,"size":size}
# #     if q:
# #         results.update({"q": q})
# #     return results


# # class Item(BaseModel):
# #     name : str
# #     description : str | None = None
# #     price : float
# #     tax : float | None = None


# # class User(BaseModel):
# #     name : str
# #     full_name : str | None  = None


# # @app.put("/items{item_id}")
# # async def update_item(*,
# #                     item_id : int=Path(..., title = "a messy txt",ge =1, le =50),
# #                     q:str | None = None,
# #                     item: Item | None = None,
# #                     user: User | None = None,
# #                     importance : int = Body(...)
# # ):
# #     results = {"item_id": item_id}
# #     if q:
# #         results.update({"q":q})
# #     if item:
# #         results.update({"item":item})
# #     if user:
# #         results.update({"user": user})
# #     if importance:
# #         results.update({"importance":importance})


# # class Item(BaseModel):
# #     name : str
# #     description: str | None = Field(None,title="the description of the item", max_length = 300)
# #     price : float | None = Field(...,gt=0, title = "price geater than 0")
# #     tax : float| None = None

# # @app.put("/item{item_id}")
# # async def update_item(item_id: int, item:Item = Body(..., embed = True)):
# #     results = {"item_id":item_id,"item":item}
# #     return results

# # class Image(BaseModel):
# #     url: str
# #     name: str
# # class Item(BaseModel):
# #     name: str
# #     description : str | None = None
# #     tax: float
# #     price : float | None = None
# #     tags: set[str] = []
# #     image: list[Image] |None = None

# # class Offer(BaseModel):
# #     name: str
# #     description : str|None = None
# #     price : float
# #     items:list[Item]


# # @app.put("/item{item_id}")
# # async def update_item(item_id: int, item:Item):
# #     results = {"item_id": item_id, "item":item}
# #     return results

# # @app.post("/offers")
# # async def create_offer(offer: Offer):
# #     return offer

# # class Item(BaseModel):
# #     name : str
# #     description : str | None = None
# #     price : float
# #     tax : float | None  = None

# #     class Config:
# #         shema_extra = {
# #             "example":{
# #                 "name":"Foo",
# #                 "description": "A very nice Item",
# #                 "price": 16.34,
# #                 "tax":1.67
# #             }
# #         }

# # @app.put("/items/{item_id}")
# # async def item_update(item_id: int, item:Item=Body(...,example ={"name":"foo","description":"faster","price":22.34,"tax":3.43})):
# #     results = {"item_id":item_id,"item":item}
# #     return results


# # @app.put("/items//{item_id}")
# # async def read_items(
# #     item_id: UUID,
# #     start_date: datetime | None = Body(None),
# #     end_date: datetime | None = Body(None),
# # ):
# #     return {"item_id": item_id, "start_date": start_date}

# @app.get("items")
# async def read_items(
#     cookie_id: str | None = Cookie(None),
#     accept_encoding : str | None  = Header(None)):
#     return {"cookie_id":cookie_id,
#         "accept_encoding":accept_encoding}


# class Item(BaseModel):
#     name : str
#     description: str | None = None
#     price: float
#     tax: float| None = None
#     tags: list[str] = []

# @app.post("/items/",response_model = Item)
# async def create_item(item: Item):
#     return item


# class UserIn(BaseModel):
#     username : str
#     password: str
#     email : EmailStr
#     full_name: str|None = None


# @app.post("/user/", response_model = UserIn)
# async def create_user(user:UserIn):
#     return user


# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None


# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None

# class UserInDB(BaseModel):
#     username: str
#     hashed_password: str
#     email: EmailStr
#     full_name: str | None = None


# def fake_password_hasher(raw_password: str):
#     return f"supersecret{raw_password}"

# def fake_save_user(user_in:UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(),hashed_password = hashed_password)
#     print("user_in.dict:",user_in.dict())
#     print("user saved")
#     return user_in_db

# @app.post("/users/",response_model= UserOut)
# async def create_user(user_in:UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved



# statsus_code
# @app.get("/items", status_code =201)
# async def read_items(name:str):
#     return {"name":name}

# @app.post("/items", status_code =204)
# async def create_items(name:str):
#     return {"name":name}

# form fields

@app.get("/login")
async def login(username:str=Form(...), password:str=Form(...)):
    return {"username":username}

