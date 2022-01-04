import dataset
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Author(BaseModel):
    name: str

class Book(BaseModel):
    title: str
    author: Author

db = dataset.connect('sqlite:///sqlite3.db')
if 'author' not in db:
    _ = db['author']
if 'book' not in db:
    _ = db['book']

@app.get("/health")
def root():
    return {"health": "alive"}

@app.get("/author/list")
def author_list():
    return list(db['author'].all())

@app.post("/author/create")
def author_create(author: Author):
    author_dict = author.dict()
    db['author'].insert(author_dict)
    return author_dict

@app.get("/author/{author_id}")
def author_detail(author_id: int):
    return list(db['author'].find(id=author_id))

@app.delete("/author/{author_id}")
def author_delete(author_id: int):
    return db['author'].delete(id=author_id)

