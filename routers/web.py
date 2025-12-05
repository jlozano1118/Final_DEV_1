from fastapi import APIRouter, Form, File, UploadFile, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlmodel import Session, select
from fastapi.templating import Jinja2Templates
from utils.db import get_session
from supa.supabase import upload_to_bucket
from data.models import Jugador, Equipo, Estadistica, Partido, Tarjeta, EquipoJugador
from datetime import date, datetime, timedelta
import calendar
from typing import Optional
from utils.states import States, Color

from sqlalchemy import func, desc  
import math  
import re



router = APIRouter(
    prefix="/web",
    tags=["Web Interface"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/jugadores", response_class=HTMLResponse)
async def pagina_jugadores(request: Request, session: Session = Depends(get_session)):
    activos = session.exec(select(Jugador).where(Jugador.estado == "ACTIVO" ).all()
    inactivos = session.exec(select(Jugador).where(Jugador.estado == "INACTIVO")).all()
    return templates.TemplateResponse("usuarios.html", {"request": request, "jugadores_activos": activos,
                                                        "jugadores_inactivos": inactivos})
