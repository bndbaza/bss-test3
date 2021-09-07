from typing import List
from fastapi import FastAPI, File, UploadFile
from models import *
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


@app.get("/entry", response_model=List[Entry_Pydantic])
async def get_entrys():
    return await Entry_Pydantic.from_queryset(Entry.all())


@app.get('/entry/{id}', response_model=Entry_Pydantic)
async def get_entry(id: int):
    return await Entry_Pydantic.from_queryset_single(Entry.get(Id=id))


@app.post('/entry', response_model=Entry_Pydantic)
async def create_entry(entry: EntryIn_Pydantic):
    entry_obj = await Entry.create(**entry.dict(exclude_unset=True))
    return await Entry_Pydantic.from_tortoise_orm(entry_obj)


@app.post('/entry/123')
async def create_file(file: UploadFile = File(...)):
    return {'filename': file.filename}


register_tortoise(
    app,
    db_url="mysql://root:35739517@192.168.0.51:3307/InOut2",
    modules={"models": ["models"]},
)