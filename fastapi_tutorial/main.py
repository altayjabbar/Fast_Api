from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/")
async def post():
    return {"message":"hello by post owner"}


@app.put("/")
async def post():
    return {"message":"put fist post"}

@app.delete("/")
async def delete():
    return {"message":"delete all post"}