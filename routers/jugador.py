# from fastapi import APIRouter, Depends, HTTPException
# from sqlmodel import Session, select
# from typing import List
# from datetime import datetime
# from utils.db import get_session
# from data.models import Jugador
# router = APIRouter(
#     prefix="/web/Jugadores",
#     tags=["Jugadores"]
# )


# @router.get("/", response_model=List[Jugador], summary="Listar todos los usuarios")
# def listar_usuarios(session: Session = Depends(get_session)):
#     Jugador = session.exec(select(Jugador).where(Jugador.is_active == True)).all()
#     return Jugador or []
