from fastapi import FastAPI
from db import create_tables

app = FastAPI(lifespan=create_tables, title="sigmotoa FC")


@app.get("/")
async def root():
    return {"message": "sigmotoa FC data"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Bienvenido a sigmotoa FC {name}"}
