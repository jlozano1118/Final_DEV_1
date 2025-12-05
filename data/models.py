
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date, datetime
from utils.states import States

class Jugador():
    id_jugador: Optional[int] = Field(default=None, primary_key=True, index=True)
    nombre_completo: str
    dorsal: int = Field(unique=True, index=True)
    fecha_nacimiento: date
    nacionalidad: str
    altura : float
    peso : int
    posicion: str
    estado: str = Field(description="Estado", default= States.ACTIVO.value)
    pie_dominate: str
    valor_mercado: float
    estadisticas : List["Estadistica"] = Relationship(back_populates="jugador")
    equipo : List["Equipo"] = Relationship(back_populates="jugador")

class Estadistica():
    pass


class Partido():
    pass


class Equipo():
    pass

class Tarjetas():
    pass
