from typing import List
from fastapi import FastAPI
from models import *
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


@app.get("/entry", response_model=List[Entry_Pydantic])
async def get_entry():
    return await Entry_Pydantic.from_queryset(Entry.all())


register_tortoise(
    app,
    db_url="mysql://root:35739517@192.168.0.51:3307/InOut2",
    modules={"models": ["models"]},
)