
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date, datetime

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
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    id_jugador:  list["Jugador"] = Relationship(back_populates="Jugador")
    id_partido:list["Partido"] = Relationship(back_populates="Partido")
    minutos: int
    goles: int
    faltas: int
    id_tarjetas:list["Tarjetas"] = Relationship(back_populates="Tarjetas")

class Tarjetas():
    pass


class Partido():
    pass



class Equipo():
    pass

class Tarjetas():
    pass

