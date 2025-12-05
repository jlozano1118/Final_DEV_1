from fastapi import FastAPI, UploadFile, File, Form, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select
from utils.db import crear_db, get_session
from data.models import Usuario, PeliculaSerie, Valoracion, Rutina
from routers import usuario, peliculaSerie, valoracion, rutina, web
import images
from sqlalchemy import func, desc
app = FastAPI(lifespan=create_tables, title="sigmotoa FC")


@app.get("/")
async def root():
    return {"message": "sigmotoa FC data"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Bienvenido a sigmotoa FC {name}"}
